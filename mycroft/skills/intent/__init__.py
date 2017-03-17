# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


from adapt.engine import IntentDeterminationEngine

from mycroft.messagebus.message import Message
from mycroft.skills.core import open_intent_envelope, MycroftSkill
from mycroft.util.log import getLogger

import time


__author__ = 'seanfitz'

logger = getLogger(__name__)


class IntentSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self, name="IntentSkill")
        self.engine = IntentDeterminationEngine()
        self.reload_skill = False
        self.active_skills = [] # [skill_id , timestamp]
        self.intent_to_skill_id = {} # intent:source_skill_id
        self.converse_timeout = 5 # minutes to prune active_skills

    def initialize(self):
        self.emitter.on('register_vocab', self.handle_register_vocab)
        self.emitter.on('register_intent', self.handle_register_intent)
        self.emitter.on('recognizer_loop:utterance', self.handle_utterance)
        self.emitter.on('detach_intent', self.handle_detach_intent)
        self.emitter.on('converse_status_response', self.handle_conversation_response)

    def do_conversation(self, utterances, skill):
        self.emitter.emit(Message("converse_status_request", {
                          "skill_id": skill, "utterances": utterances}))
        self.waiting = True
        self.result = False
        while self.waiting:
            pass
        return self.result

    def handle_conversation_response(self, message):
        # id = message.data["skill_id"]
        # no need to crosscheck id because waiting before new request is made
        # no other skill will make this request is safe assumption
        result = message.data["result"]
        self.result = result
        self.waiting = False

    def remove_active_skill(self, skill_id):
        for skill in self.active_skills:
            if skill[0]==skill_id:
                self.active_skills.remove(skill)

    def add_active_skill(self, skill_id):
        # you have to search the list for an existing entry that already contains it and remove that reference
        self.remove_active_skill(skill_id)
        # add skill with timestamp to start of skill_list
        self.active_skills.insert(0, [skill_id, time.time()])

    def handle_utterance(self, message):

        utterances = message.data.get('utterances', '')
        # check for conversation time-out
        self.active_skills = [skill for skill in self.active_skills
                              if time.time() - skill[1] <= self.converse_timeout * 60]

        # check if any skill wants to handle utterance
        for skill in self.active_skills:
            if self.do_conversation(utterances, skill[0]):
                # update timestamp, or there will be a timeout where
                # intent stops conversing wether its being used or not
                self.add_active_skill(skill[0])
                return
        # no skill wants to handle utterance, proceed

        best_intent = None
        for utterance in utterances:
            try:
                best_intent = next(self.engine.determine_intent(
                    utterance, 100))
                # TODO - Should Adapt handle this?
                best_intent['utterance'] = utterance

            except StopIteration, e:
                logger.exception(e)
                continue

        if best_intent and best_intent.get('confidence', 0.0) > 0.0:
            reply = message.reply(
                best_intent.get('intent_type'), best_intent)
            self.emitter.emit(reply)

            # best intent detected -> update called skills dict
            skill_id = self.intent_to_skill_id[best_intent['intent_type']]
            self.add_active_skill(skill_id)
            # process feedback
            if best_intent['intent_type'] == "PositiveFeedbackIntent" or best_intent['intent_type'] == "NegativeFeedbackIntent":
                self.emitter.emit(Message("feedback_id",{"active_skill":self.active_skills[1][0]}))
            # convert intent to objective and execute

        elif len(utterances) == 1:
            self.emitter.emit(Message("intent_failure", {
                "utterance": utterances[0]
            }))
        else:
            self.emitter.emit(Message("multi_utterance_intent_failure", {
                "utterances": utterances
            }))

    def handle_register_vocab(self, message):
        start_concept = message.data.get('start')
        end_concept = message.data.get('end')
        regex_str = message.data.get('regex')
        alias_of = message.data.get('alias_of')
        if regex_str:
            self.engine.register_regex_entity(regex_str)
        else:
            self.engine.register_entity(
                start_concept, end_concept, alias_of=alias_of)

    def handle_register_intent(self, message):
        intent = open_intent_envelope(message)
        self.engine.register_intent_parser(intent)
        # map intent to source skill
        self.intent_to_skill_id.setdefault(
            intent.name, message.data["source_skill"])

    def handle_detach_intent(self, message):
        intent_name = message.data.get('intent_name')
        new_parsers = [
            p for p in self.engine.intent_parsers if p.name != intent_name]
        self.engine.intent_parsers = new_parsers

    def stop(self):
        pass


def create_skill():
    return IntentSkill()

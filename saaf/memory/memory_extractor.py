import re

from saaf.models.memory import Memory
from saaf.memory.memory_types import MemoryType


class MemoryExtractor:
    """
    Extract user profile information.
    """


    def extract(self, user_id, text):

        text_lower = text.lower()


        # -----------------------------
        # Name
        # -----------------------------

        match = re.search(
           r"my name\s+is\s+(.+)",
            text,
            re.IGNORECASE
        )


        if match:

            return Memory(

                user_id=user_id,

                memory_key="name",

                memory_value=match.group(1).strip(),

                memory_type=MemoryType.FACT,

                importance=10

            )


        # -----------------------------
        # Skills
        # -----------------------------

        match = re.search(
            r"i know (.+)",
            text,
            re.IGNORECASE
        )


        if match:

            skills = [

                item.strip()

                for item in match.group(1).split(",")

            ]


            return Memory(

                user_id=user_id,

                memory_key="skills",

                memory_value=skills,

                memory_type=MemoryType.SKILL,

                importance=9

            )


        # -----------------------------
        # Goal
        # -----------------------------

        match = re.search(
            r"i want to become (.+)",
            text,
            re.IGNORECASE
        )


        if match:

            return Memory(

                user_id=user_id,

                memory_key="goal",

                memory_value=match.group(1).strip(),

                memory_type=MemoryType.GOAL,

                importance=8

            )


        return None
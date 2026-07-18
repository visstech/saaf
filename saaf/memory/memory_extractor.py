import re

from saaf.models.memory import Memory


class MemoryExtractor:
    """
    Extract structured memories
    from user messages.
    """


    def extract(self, user_id: str, text: str):
        """
        Extract memory from text.

        Returns:
            Memory | None
        """

        text = text.strip()


        # -----------------------------
        # Name Extraction
        # -----------------------------

        match = re.search(

            r"my name is (.+)",

            text,

            re.IGNORECASE

        )
        #print(match)

        if match:

            name = match.group(1).strip()


            return Memory(

                user_id=user_id,

                memory_key="name",

                memory_value=name,

                memory_type="fact",

                importance=10

            )


        return None
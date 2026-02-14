from typing import List

class GapDetector:
    def find_gaps(self, target_channel_topics: List[str], competitor_topics: List[str]) -> List[str]:
        """
        Identifies topics present in competitor_topics but missing from target_channel_topics.
        Returns a list of unique missing topics.
        """
        target_set = set([t.lower() for t in target_channel_topics])
        competitor_set = set([t.lower() for t in competitor_topics])
        
        # Gaps = Competitor - Target
        gaps = competitor_set.difference(target_set)
        
        return list(gaps)

gap_detector = GapDetector()

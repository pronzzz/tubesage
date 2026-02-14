from typing import List, Set

class OverlapAnalyzer:
    def calculate_overlap(self, channel_a_topics: List[str], channel_b_topics: List[str]) -> float:
        """
        Calculates the Jaccard Similarity Index between two sets of topics.
        J(A, B) = |A ∩ B| / |A ∪ B|
        """
        set_a = set([t.lower() for t in channel_a_topics])
        set_b = set([t.lower() for t in channel_b_topics])
        
        if not set_a and not set_b:
            return 0.0
            
        intersection = set_a.intersection(set_b)
        union = set_a.union(set_b)
        
        if not union:
            return 0.0
            
        return len(intersection) / len(union)

overlap_analyzer = OverlapAnalyzer()

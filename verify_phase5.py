import sys
import os

sys.path.append(os.path.join(os.getcwd(), "backend"))

print("Verifying TubeSage Competitor Intelligence Module...")

try:
    from app.core.competitors.overlap import overlap_analyzer
    from app.core.competitors.gap_detector import gap_detector
    
    print("✅ Competitor modules loaded")
    
    target = ["python", "fastapi", "docker"]
    competitor = ["python", "django", "kubernetes", "docker"]
    
    # Intersection: python, docker (2)
    # Union: python, fastapi, docker, django, kubernetes (5)
    # Overlap: 2/5 = 0.4
    
    score = overlap_analyzer.calculate_overlap(target, competitor)
    print(f"Test Overlap (Expected 0.4): {score}")
    
    # Gaps: django, kubernetes
    gaps = gap_detector.find_gaps(target, competitor)
    print(f"Test Gaps (Expected ['django', 'kubernetes']): {sorted(gaps)}")
    
except Exception as e:
    print(f"❌ Verification failed: {e}")
    raise e

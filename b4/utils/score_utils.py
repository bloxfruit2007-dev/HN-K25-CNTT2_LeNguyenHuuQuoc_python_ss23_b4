def calculate_average(*scores: float) -> float:
    valid_scores = []
    for score in scores:
        if isinstance(score, (int, float)):
            valid_scores.append(score)

    if not valid_scores:
        return 0, "Yếu"
    
    avg_score = round(sum(scores)/len(scores),2)
    
    if avg_score >= 8.0: qualification = "Giỏi"
    elif avg_score >= 6.5: qualification = "Khá"
    elif avg_score >= 5: qualification = "Trung bình"
    else: qualification = "Yếu"

    return avg_score,qualification

def cal_total(marks):
    return sum(marks)

def cal_per(marks):
    total = sum(marks)
    return (total / (len(marks) * 100)) * 100

def cal_grade(per):
    if per >= 90:
        return "A+"
    elif per>=75:
        return "B+"
    elif per >= 60:
            return "B"
    elif per >= 45:
            return "C"
    else:
            return "Fail"
    
def is_pass(marks):
    for m in marks:
        if m < 35:
            return False
    return True


# Naive Bayes Manual Calculation

p_pass = 0.6
p_fail = 0.4

# Conditional probabilities
p_maths_high_pass = 0.75
p_att_poor_pass = 0.375
p_internal_med_pass = 0.44

p_maths_high_fail = 0.17
p_att_poor_fail = 0.67
p_internal_med_fail = 0.29

# Naive Bayes
pass_result = p_pass * p_maths_high_pass * p_att_poor_pass * p_internal_med_pass
fail_result = p_fail * p_maths_high_fail * p_att_poor_fail * p_internal_med_fail

print("Pass Probability:", pass_result)
print("Fail Probability:", fail_result)

if pass_result > fail_result:
    print("Prediction = PASS")
else:
    print("Prediction = FAIL")
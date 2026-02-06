from generator_agent import ResumeGeneratorAgent
from critic_agent import ResumeCriticAgent

generator = ResumeGeneratorAgent()
critic = ResumeCriticAgent()

role = "Machine Learning Intern"

draft = generator.generate(role)
print("Draft:")
for d in draft:
    print("-",d)

issues = critic.critique(draft)
print("\nCritique:")
for i in issues:
    print("-",i)

if issues:
    final_output = [
        "Developed and trained machine learning models in Python, improving prediction accuracy by 15%",
        "Implemented data preprocessing pipelines using NumPy and Pandas, reducing training time by 20%",
        "Optimized model performance through hyperparameter tuning and cross-validation"
    ]

else:
    final_output = draft

print("\nFinal Output:")
for f in final_output:
    print("-",f)
import random
star_feedback= {1:"⭐",
                2:"⭐⭐",
                3:"⭐⭐⭐",
                4:"⭐⭐⭐⭐",
                5:"⭐⭐⭐⭐⭐"}
Eng_Arwa_Rate = star_feedback[random.randint(1,5)]
print("Rate instructor (Eng Arwa) is :\n",Eng_Arwa_Rate)
Afnan_and_salah= star_feedback[random.randint(1,5)]
print("Rate supporters (Afnan & salah)\n",Afnan_and_salah)
feedback_dict = {
    1: "The explanation was clear and easy to follow.",
    2: "Great lecture! The content was well-organized and informative.",
    3: "The instructor made complex topics feel simple.",
    4: "Appreciate the effort put into engaging with the students.",
    5: "The pace was a bit fast at times, but overall good delivery.",
    6: "Would have loved to see more real-life examples.",
    7: "Excellent teaching style — very interactive and student-focused.",
    8: "It would help if the instructor used more visuals or diagrams.",
    9: "The session helped me understand the topic better than before.",
    10: "Thank you for always answering questions so patiently.",
    11: "The content was useful, but a short recap at the end would help.",
    12: "Loved the energy and clarity of the instructor!",
    13: "Sometimes the slides were too text-heavy — maybe simplify them.",
    14: "I really appreciated the real-world applications mentioned.",
    15: "The session could have used more time for Q&A.",
}
Eng_Arwa_feedback = feedback_dict[random.randint(1,15)]
print("Instructor feedback : \n",Eng_Arwa_feedback)
section_feedback = {
    1: "The section was very interactive and helped reinforce the lecture content.",
    2: "Great explanation during the section — concepts were clearly broken down.",
    3: "The TA made sure everyone was following along, which was really helpful.",
    4: "It was a well-organized section with a good balance between theory and practice.",
    5: "The pace was suitable and the TA explained each step clearly.",
    6: "I appreciated how the TA encouraged questions and participation.",
    7: "Would be great to see more hands-on examples during the section.",
    8: "Sometimes the section felt rushed — a bit more time on exercises would help.",
    9: "The TA created a comfortable environment to ask questions.",
    10: "Helpful recap at the beginning of the section made things easier to follow.",
    11: "Some of the exercises were a bit unclear — more guidance would be appreciated.",
    12: "Very supportive TA who explained until everyone understood.",
    13: "The section added a lot of value and cleared up confusion from the lecture.",
    14: "A few technical issues affected the flow, but overall it was useful.",
    15: "The TA used great real-world examples that made the topic more relatable.",
}
section_Feedback = section_feedback[random.randint(1,15)]
print(f"Section Feedback:\n {section_Feedback}")
section_recommendations = {
    1: "Consider adding a quick summary at the end of each section to reinforce key points.",
    2: "It might help to include more hands-on coding or problem-solving exercises.",
    3: "Adding more visual aids or diagrams could improve understanding.",
    4: "Try to slow down a bit during complex explanations to make sure everyone keeps up.",
    5: "Including mini quizzes or interactive polls could make the section more engaging.",
    6: "Maybe share extra resources or practice problems for students who want to dive deeper.",
    7: "Encourage more peer discussion or group activities during the section.",
    8: "Try to give students a chance to solve problems before showing the solution.",
    9: "Recording the section (if possible) would help students review later.",
    10: "Consider checking in with quieter students to ensure they're following along.",
}
section_Recommendations = section_recommendations[random.randint(1,10)]
print("Section Recommendations : \n %s"%(section_Recommendations))
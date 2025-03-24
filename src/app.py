"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice and compete in basketball tournaments",
        "schedule": "Wednesdays and Fridays, 3:00 PM - 4:30 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore your creativity through painting and drawing",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
    },
    "Drama Club": {
        "description": "Learn acting skills and participate in school plays",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["ella@mergington.edu", "scarlett@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging math problems and prepare for competitions",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Fridays, 3:00 PM - 4:30 PM",
        "max_participants": 12,
        "participants": ["elijah@mergington.edu", "lucas@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Learn and practice tennis skills with professional coaching",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["grace@mergington.edu", "chloe@mergington.edu"]
    },
    "Swimming Team": {
        "description": "Train and compete in swimming competitions",
        "schedule": "Mondays, Wednesdays, Fridays, 3:00 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["jackson@mergington.edu", "aiden@mergington.edu"]
    },
    "Photography Club": {
        "description": "Learn photography techniques and showcase your work",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["lily@mergington.edu", "zoe@mergington.edu"]
    },
    "Music Band": {
        "description": "Join the school band and perform at events",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["henry@mergington.edu", "victoria@mergington.edu"]
    },
    "Debate Club": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["charlotte@mergington.edu", "william@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Build and program robots for competitions",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["ethan@mergington.edu", "alexander@mergington.edu"]
    },
    "Volleyball Team": {
        "description": "Practice and compete in volleyball tournaments",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["oliver@mergington.edu", "lucy@mergington.edu"]
    },
    "Track and Field": {
        "description": "Train for track and field events and compete in meets",
        "schedule": "Mondays, Wednesdays, Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": ["logan@mergington.edu", "hannah@mergington.edu"]
    },
    "Painting Workshop": {
        "description": "Learn advanced painting techniques and create masterpieces",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["nora@mergington.edu", "leo@mergington.edu"]
    },
    "Creative Writing Club": {
        "description": "Write stories, poems, and essays and share them with peers",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["ella@mergington.edu", "samuel@mergington.edu"]
    },
    "Astronomy Club": {
        "description": "Explore the universe and learn about celestial objects",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["sophia@mergington.edu", "liam@mergington.edu"]
    },
    "History Club": {
        "description": "Dive into historical events and discuss their impact",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["emma@mergington.edu", "noah@mergington.edu"]
    },
    # New activities
    "Badminton Club": {
        "description": "Learn and play badminton with peers",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["olivia@mergington.edu", "ethan@mergington.edu"]
    },
    "Cycling Club": {
        "description": "Explore local trails and improve cycling skills",
        "schedule": "Saturdays, 8:00 AM - 10:00 AM",
        "max_participants": 20,
        "participants": ["amelia@mergington.edu", "lucas@mergington.edu"]
    },
    "Sculpture Workshop": {
        "description": "Learn to create sculptures using various materials",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["mia@mergington.edu", "jackson@mergington.edu"]
    },
    "Dance Club": {
        "description": "Practice and perform various dance styles",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "liam@mergington.edu"]
    },
    "Philosophy Club": {
        "description": "Discuss philosophical ideas and their relevance",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["sophia@mergington.edu", "noah@mergington.edu"]
    },
    "Economics Club": {
        "description": "Learn about economic principles and global markets",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["emma@mergington.edu", "william@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Validar se o aluno já está inscrito
    # Validate if the student is already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}

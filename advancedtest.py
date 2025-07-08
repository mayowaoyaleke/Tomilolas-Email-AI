import streamlit as st
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load environment variables from .env file (for local development)
load_dotenv(override=True)

# google_api_key = st.secrets["google_api_key"]
google_api_key = "AIzaSyCUQuz1oJ30wq9m17V9LiImQfboo5SLJS4"

# Page configuration
st.set_page_config(
    page_title="Tomilola's Email AI",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize Google GenAI client
@st.cache_resource
def init_genai_client():
    return genai.Client(api_key= google_api_key)

client = init_genai_client()

# Pre-trained email templates and style profile
EMAIL_TEMPLATES = """
Email 1 -
Dear Mumbi, Ajo, Albert, and Tomilayo,
I trust you're all doing great! It was such a pleasure meeting and speaking with you yesterday. We enjoyed having you over.
Although I joined midway, I found our conversation insightful and interesting. From what I gathered, there’s clear alignment between our visions, and I’m excited about what we can build together. Here's a quick recap of the key areas I noted:

Funnel & Distribution Partnership:
Learners from PLP can transition into diploma programs at AltSchool Africa to further their education.
Conversely, we can also direct learners toward specific specializations or initiatives that PLP offers.
This also covers collaboration on learner outcomes, from careers to real-world projects like hackathons, demo days, or build competitions.

Community Partnerships:
We can implement in-person community initiatives, leveraging our local spaces and networks across countries.
This could include events, spotlights, or activations that showcase the impact and mission of both organizations.

Entrepreneurship Opportunities:
Though still a broad idea, we touched on the potential for jointly supporting learner entrepreneurship, perhaps through innovation challenges or venture-building programs.

Please feel free to share anything I may have missed or misunderstood.
I’m looping in our Senior Community Manager, as well as our Kenya Lead. @Tabitha Kavyu. Also copied are our business powerhouses in Rwanda, @Christine Ashimwe and @Sandrine Ingabire.

Let’s plan to have a call sometime next week to align on immediate opportunities and refine the broader partnership scope. I’ll follow up shortly with a few suggested times.

In the meantime, could you please share a brochure or deck that gives us deeper insight into your programs and initiatives at Power Learn Project? It’ll help us better familiarize ourselves ahead of our next conversation.
Looking forward to what we can build together.
Warm regards,


Email 2 -
Dear Beatrice,
Tomi here, from AltSchool Africa! My colleague mentioned meeting you at the Lagos Startup Expo a couple of weeks ago. I appreciated the conversations we had and the insights you shared about CloudPlexo's work.

I wanted to follow up on the possibility of accessing discounted AWS Cloud credits for our learner community, particularly those in our School of Engineering. From our discussion, it sounded quite feasible once we meet the relevant requirements, and we’re keen to explore the next steps.

Looping in our School of Engineering Program Manager, @Amara Onyeji, and our Senior Program Manager, @Susan Odere, so we can coordinate any information or documentation needed on our end.

Looking forward to hearing from you.
Warm regards,



Hello [Name],

I hope you're doing well. I'd like to schedule a meeting to discuss the upcoming project milestones and ensure we're all aligned on the next steps.

Would you be available for a 30-minute call sometime next week? I'm flexible with timing and can work around your schedule.

Please let me know what works best for you.

Thank you,
[Your name]


Email 3 - 

Hi Abdulwahid and Wemimo,
Tomi here from AltSchool Africa! I hope you’re both doing great. It was such a pleasure to meet you and the Cardify team last week (again!)

At this point, it feels like we’re so aligned that a collaboration is long overdue. Don’t you think?

We touched on a few ideas during our chat, and I’d love for us to build on them:

 AltSchoolers @ Cardify – A Co-branded Campaign
It’s genuinely exciting to see that at least five AltSchoolers have worked (or currently work) with your team, and clearly, they’re doing amazing work. We'd love to co-create a campaign spotlighting their stories and the excellence both Cardify and AltSchool stand for.

I’ve looped in @Adewunmi Adewale (our Head of Marketing) and @Sandrine Ingabire (from our Career Services team) to shape the creative direction with you. For reference, here’s a similar campaign we did with  Octosoft [watch here].

Powering Learner Tools' Payments with Cardify
We also talked about Cardify supporting learners with virtual cards for international payments, especially for cloud services and engineering tools.

A lot of Nigerian learners struggle with failed transactions using traditional or even some virtual cards. If Cardify can offer a reliable, widely accepted solution, it would be a game-changer.
Would you be able to confirm the range of platforms your cards work with? A test card and/or a customized plan would be super helpful at this stage. Looping in @Susan Odere for oversight here.

We’re also open to supporting the Cardify team through formalized corporate training. AltSchool could become your go-to learning and development partner for group/team training.

Of course, this is just the beginning. I’d love for us to explore the possibilities in more detail. Feel free to book a call for later this week or early next here.

Looking forward to building something exciting together!

Warm regards,


Email 4 - 
Hello Lois,
I trust you're well.

Thank you for reaching out. I completely understand your concern. From what I can tell, it’s likely that the code you received initially was set up to cover a quarter. Since your sponsorship is through your employer, we’re required to track your engagement and performance by issuing quarterly access codes. This means you’ll need to request a new waiver code each quarter for continued access.

I recognize this may not have been communicated earlier, and I sincerely apologize for any confusion.

That said, please meet Jessica, our Scholarships Coordinator. We'll work together to confirm if this is the case and ensure you receive a new code shortly so you can resume learning without delay.

Thank you again for your patience, and you’ll hear back from us soon.

Warm regards,


Email 5 -
Hello Stanley,

Thank you for reaching out with this, much appreciated!

Yes, we already have a good number of our courses live, and more are being rolled out. You can check them out at courses.altschoolafrica.com.

I also plan to attend Lagos Startup Week. I think it would be great to share the spotlight with you during the Creative Economy session. I’ve registered via the link you shared and will be sharing this with a few members of my team as well.

Looping in our Head of Marketing @Adewunmi Adewale, to also take a look at the opportunity. I believe when we connect in person, we can have a more robust conversation about what's next for the Aktivate community.

Warm regards,


Email 6 -
Hi Osaro,
It was great catching up with you, and I appreciate the alignment we’ve built so far.

As agreed, we're taking a new, strategic approach to fill up the remaining scholarship seats ahead of the next cohort — with minimal lift required from your end.

Here’s the plan:
1. We’ll relaunch marketing efforts on our end, this time with targeted campaigns — region- and demography-specific (especially East Africa). These campaigns will spotlight the key benefits of the Fund and the unique value of each program.

Our Senior Marketing Manager. @Adewunmi Adewale  also recommends a complementary email marketing push. On our side, we’ll re-engage unpaid applicants in those key regions, and we propose doing the same with your community. We’ll share a tested email series with you for your use, tailored to drive quality applications.

2. On lead capture & applicant management, we’ll own the entire process with your oversight. We’ll create a preliminary application form and add you as a collaborator to review and approve the fields, including any Binance-specific touchpoints (e.g., uploading a screenshot of their Binance profile or providing their user ID upon registration).

Once applications hit the required number, we’ll handle shortlisting, ensure a smooth admissions process, and keep everything moving seamlessly.

You’ll be looped in throughout, so you’re always informed but never burdened.

Please confirm you're aligned, and let us know if you have any suggestions or adjustments. Once you give the green light, we’ll share the form with you later today and keep it moving from there.

Warm regards,


Email 7 -
Hello Seun,
I trust you're doing great!

First off, a huge congratulations to you and the entire Cleva team on this incredible two-year milestone coming up in August. You’re doing amazing work, and it’s been inspiring to watch your journey and be part of it.

We’d be honoured to attend the anniversary event. By Monday next week, I’ll send over the names of the two team members who’ll be attending on our end.

Also, thank you for sharing the Cleva Business Challenge. It looks fantastic! We have so many brilliant entrepreneurs, startup teams, and self-starters within the AltSchool community, and this is a good opportunity for them. I’ll be sharing this with my team (also copied here), and I’m confident we’ll have some strong participants.

I’ll be in touch shortly with the attendee details.
Best regards,

Email 8 -
Hi Olamide,
Tomi here from AltSchool Africa! I hope your week’s going well! It was a pleasure meeting you at the Lagos Startup Expo last week.

As promised, I’m following up to share more details about our Cryptocurrency Education Program, an initiative designed to demystify decentralized finance and empower millions of Africans with practical, relevant crypto knowledge.

Partnering with us means Divest would be integrated into the experience, from course branding to learning content and community engagement, giving your brand visibility at scale and a direct path to new users.

I've attached a proposal outlining the course structure, audience reach, and how we envision Divest collaborating.

I’d love to learn more about Divest’s growth goals and see how this aligns. Feel free to book a call at your convenience via this link [here].

Looking forward to building something impactful together.
Best regards,

Email 9 -
Hello Godbless and team,
I trust you're doing fine and your week is off to a great start!
Thanks once again for hosting us at your office last Friday. It was a real pleasure learning more about Aella and knowing that you're just as excited about working with us as we are with you.
Just as a recap, we discussed:
Aella powering courses at AltSchool Africa. Sponsorship criteria will include prospective recipients signing up and transacting with Aella. This works for us, as we trust your organization and see the importance of this partnership being mutually beneficial.
CSR collaboration. Aella is also open to running CSR projects with us (private-public impact partnerships).
Banking with Aella. AltSchool is considering creating an account with Aella MFB and managing collections, particularly for this partnership, through Aella.
Corporate training. We also explored coming onboard as a corporate training partner for your technical and business teams, including general knowledge-sharing sessions, individual learning and development, and team-custom training.
As next steps:
Our team is exploring account opening with Aella. However, as we mentioned, they'd love to understand the perks and finer details for corporate account holders.
We'd also love to put numbers and dates to our partnership, finalizing the details and agreeing on a rollout plan.
We're off to a great start, and we look forward to seeing where this goes. Our Finance and Business Operations team will be in next Tuesday, 1st of July 2025. We'd be glad to have you over, and move forward with the next steps. In the meantime, we’d appreciate any documentation or info around corporate account benefits to support internal alignment.
How does that sound?
We’ll be on standby!
Best regards,

Emain 10 -
Hi Adanna,
Tomi here from AltSchool! I hope you’re doing great and have had a chance to rest since the Lagos Startup Expo. It was really lovely meeting you!
I’ve been thinking about our chat, and honestly, Moniger stands out. A single platform that makes personal finance simpler, from budgeting to tracking expenses across multiple accounts. This is the kind of value we believe young Africans need.
I also think there’s a lot we can do together. For starters:
Moniger could power courses in our Creative Economy or Business School, with built-in co-marketing and direct community engagement to drive visibility and adoption.
We could also create a custom learning experience for your users on your platform; bite-sized content on financial literacy (powered by Moniger), plus practical skills like entrepreneurship and digital tools to help them grow wealth sustainably.
It’s a win on both sides: increased engagement and transaction volume for Moniger, and more value for our learners. There are a few more ideas I’d love to share, including creative brand storytelling, hiring support, and corporate training. I'd also really love to know what your thoughts are on partnership. How would you like to work with us?
Are you open to a quick call this week or next? This is a link to book a time that works for you: [here].
Looking forward to exploring this further!
Warm Regards,

Email 11 -
Hello Francis,
It was a pleasure meeting you at the LSE!
Thank you for sharing more about SOS Children’s Villages. I must commend the incredible work your organization is doing to transform lives and restore hope globally. It would be our pleasure to collaborate with you in the near future.
We're particularly keen on exploring empowerment initiatives with you. That said, it would be helpful to understand how such initiatives are typically funded or sponsored on your end. We'd also be glad to support your team in the fundraising process by co-developing a working plan and budget for a potential AltSchool–SOS Children’s Villages initiative, for instance, a summer tech bootcamp for kids. This could then be formalized in a memorandum of understanding and used to engage prospective funding partners or donors.
In the meantime, should any internal initiative arise that aligns with the Nigerian child, I won’t hesitate to reach out and explore opportunities for collaboration.
I’ll be on standby to hear back from you, and please feel free to share any questions or thoughts you may have.
Best regards,


Email 12 -
Hello Chioma and Timothy,
I hope you're doing well.
We recently submitted a request for access to LinkedIn Sales Navigator, primarily to support the AltSchool Europe team in prospecting and engaging leads for Pipeline 3.0, targeting both corporate and individual learners, home and abroad, as well as for the upcoming Data & AI cohort launching in August.
Beyond these priorities, the tool will also be instrumental to my broader partnership goals, particularly in engaging already identified enterprise partners.
We’ve received approval for a one-month trial (as referenced in the email above). However, I’ve previously used my LinkedIn trial for role-relevant learning with LinkedIn Learning, so reactivation now requires a paid monthly subscription (with the option to discontinue/cancel subscription after the first month). Please find the plan details below.
I’m requesting your support in activating the first month. Future subscription decisions can be based on the impact and outcomes from this initial phase. The tool will be instrumental in helping us reach the right audiences and drive conversion toward, first, our Pipeline 3.0 program.
Happy to share any additional details if needed. Thanks for your continued support.
Warm regards,


"""

# System instruction for email generation with pre-trained style
system_instruction = f"""
You are Tomilola's personal email writing assistant (Tomilola is an experienced Relationship Manager and heads the partnership department in the organization she works for). You have been trained on her specific email communication style and tone. Generate emails that match her professional yet warm writing pattern.

TOMILOLA'S EMAIL STYLE PROFILE:
Based on the following email examples, you understand her communication style:

{EMAIL_TEMPLATES}

WRITING CHARACTERISTICS:
1. TONE: Professional yet warm and approachable
2. STRUCTURE: Clear and concise with logical flow
3. OPENINGS: Friendly greetings with context setting
4. BODY: Well-organized with bullet points when needed
5. CLOSINGS: Polite and professional sign-offs
6. LANGUAGE: Clear, direct, and professional vocabulary
7. FORMATTING: Clean structure with appropriate spacing

GENERATION RULES:
- Always include a relevant subject line
- Start with appropriate greeting
- Provide clear context and purpose
- Use professional but warm tone
- Include specific action items when relevant
- End with appropriate closing
- Match the style and tone from the examples
- Keep emails concise but thorough
- Use proper email formatting

Generate emails that authentically match this learned style while adapting to the specific context provided.
"""

# Functions for email AI
def generate_email(context, key_points=None, special_instructions=None, urgency="normal"):
    """Generate an email based on context using pre-trained style"""
    email_prompt = f"""
    Generate a professional email using Tomilola's established communication style with the following specifications:

    CONTEXT: {context}
    KEY POINTS: {key_points if key_points else 'Determine from context'}
    URGENCY: {urgency}
    SPECIAL INSTRUCTIONS: {special_instructions if special_instructions else 'None'}
    
    Generate a complete email including:
    - Subject line
    - Full email body with proper formatting
    - Appropriate greeting and closing
    
    Ensure the email matches Tomilola's professional yet warm communication style as demonstrated in the training examples.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.3,
                top_p=0.9,
                top_k=50,
                max_output_tokens=1024,
            ),
            contents=email_prompt
        )
        return response.text
    except Exception as e:
        return f"Error generating email: {str(e)}"

def quick_generate_email(prompt):
    """Quick email generation using pre-trained style"""
    enhanced_prompt = f"""
    Using Tomilola's established email communication style, {prompt}
    
    Make sure to include:
    - Appropriate subject line
    - Professional greeting
    - Clear and concise body
    - Proper closing
    
    Match the tone and style from the training examples.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.3
            ),
            contents=enhanced_prompt
        )
        return response.text
    except Exception as e:
        return f"Error generating email: {str(e)}"

# Apple-inspired CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #fafafa 0%, #f5f5f7 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    .block-container {
        max-width: 900px;
        padding: 3rem 2rem;
    }
    
    .hero-section {
        text-align: center;
        padding: 2rem 0 3rem 0;
        background: transparent;
    }
    
    .hero-title {
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 700;
        line-height: 1.1;
        letter-spacing: -0.02em;
        margin-bottom: 1rem;
    }
    
    .hero-title .steel-grey {
        color: #71717a;
    }
    
    .hero-title .orange {
        color: #f97316;
    }
    
    .hero-subtitle {
        font-size: 1.375rem;
        font-weight: 400;
        color: #86868b;
        margin-bottom: 3rem;
        line-height: 1.4;
    }
    
    .content-section {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.06);
    }
    
    .input-label {
        font-size: 1.125rem;
        font-weight: 600;
        color: #1d1d1f;
        margin-bottom: 0.75rem;
        display: block;
    }
    
    .stTextArea > div > div > textarea {
        border: 2px solid #e5e5e7;
        border-radius: 16px;
        padding: 1.5rem;
        font-size: 1rem;
        font-family: 'Inter', sans-serif;
        line-height: 1.6;
        background: linear-gradient(135deg, #f5f5f7 0%, #ffffff 100%);
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        resize: vertical;
        min-height: 200px !important;
        height: 200px;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #f97316;
        box-shadow: 0 0 0 4px rgba(249, 115, 22, 0.15);
        outline: none;
        background: #ffffff;
    }
    
    .stTextArea > div > div > textarea::placeholder {
        color: #86868b;
        font-style: normal;
    }
    
    .stTextInput > div > div > input {
        border: 2px solid #e5e5e7;
        border-radius: 16px;
        padding: 1rem 1.5rem;
        font-size: 1rem;
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #f5f5f7 0%, #ffffff 100%);
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #f97316;
        box-shadow: 0 0 0 4px rgba(249, 115, 22, 0.15);
        outline: none;
        background: #ffffff;
    }
    
    .button-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 1.5rem 0;
        flex-wrap: wrap;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #007aff 0%, #0056cc 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 2rem;
        font-size: 1rem;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        box-shadow: 0 4px 20px rgba(0, 122, 255, 0.3);
        min-width: 180px;
        letter-spacing: 0.02em;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(0, 122, 255, 0.4);
        background: linear-gradient(135deg, #0056cc 0%, #003d99 100%);
    }
    
    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 4px 15px rgba(0, 122, 255, 0.3);
    }
    
    .stButton > button:disabled {
        background: #e5e5e7;
        color: #86868b;
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }
    
    .output-label {
        font-size: 1.125rem;
        font-weight: 600;
        color: #1d1d1f;
        margin-bottom: 1.5rem;
        display: block;
    }
    
    .output-container {
        background: linear-gradient(135deg, #f5f5f7 0%, #ffffff 100%);
        border: 1px solid #e5e5e7;
        border-radius: 16px;
        padding: 2rem;
        min-height: 180px;
        font-size: 1rem;
        line-height: 1.6;
        color: #1d1d1f;
        font-family: 'Inter', sans-serif;
        white-space: pre-wrap;
    }
    
    .output-text {
        color: #1d1d1f;
        font-weight: 400;
    }
    
    .output-placeholder {
        color: #86868b;
        font-style: italic;
        font-weight: 400;
    }
    
    .tabs-container {
        margin-bottom: 2rem;
    }
    
    .footer {
        text-align: center;
        color: #86868b;
        font-size: 0.9rem;
        margin-top: 4rem;
        padding: 2rem 0;
        font-weight: 400;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Loading spinner */
    .stSpinner > div {
        border-color: #007aff transparent transparent transparent;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .block-container {
            padding: 2rem 1rem;
        }
        
        .content-section {
            padding: 1.5rem;
        }
        
        .hero-section {
            padding: 2rem 0 3rem 0;
        }
        
        .stButton > button {
            padding: 1rem 1.5rem;
            font-size: 0.9rem;
            min-width: 140px;
        }
        
        .button-container {
            flex-direction: column;
            align-items: center;
        }
        
        .stTextArea > div > div > textarea {
            min-height: 160px !important;
            height: 160px;
        }
        
        .output-container {
            min-height: 140px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_email' not in st.session_state:
    st.session_state.generated_email = ''
if 'is_processing' not in st.session_state:
    st.session_state.is_processing = False

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title"><span class="steel-grey">Tomilola's Email</span> <span class="orange">AI</span></h1>
    <p class="hero-subtitle">Intelligent Email Writer built by her Crush 🍊.<br>Simple. Fast. Precise.</p>
</div>
""", unsafe_allow_html=True)

# Main Content
st.markdown('<div class="content-section">', unsafe_allow_html=True)

# Tab selection
tab1, tab2 = st.tabs(["📝 Quick Generate", "🎯 Detailed Generate"])

with tab1:
    st.markdown('<span class="input-label">What email do you need?</span>', unsafe_allow_html=True)
    
    quick_prompt = st.text_area(
        "",
        placeholder="Describe the email you want to generate. For example: 'Write a follow-up email to a client about project delays' or 'Send a thank you email after a meeting'",
        key="quick_prompt",
        label_visibility="collapsed",
        height=120
    )
    
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    
    if st.button("Generate Email", key="quick_generate", disabled=not quick_prompt.strip()):
        st.session_state.is_processing = True
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<span class="input-label">Email Context</span>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        context = st.text_input(
            "",
            placeholder="e.g., Client meeting follow-up",
            key="context",
            label_visibility="collapsed"
        )
    
    with col2:
        urgency = st.selectbox(
            "",
            ["normal", "urgent", "low"],
            key="urgency",
            label_visibility="collapsed"
        )
    
    st.markdown('<span class="input-label">Key Points to Include</span>', unsafe_allow_html=True)
    
    key_points = st.text_area(
        "",
        placeholder="List the main points you want to include in the email...",
        key="key_points",
        label_visibility="collapsed",
        height=100
    )
    
    st.markdown('<span class="input-label">Special Instructions (Optional)</span>', unsafe_allow_html=True)
    
    special_instructions = st.text_area(
        "",
        placeholder="Any specific requirements or additional context...",
        key="special_instructions",
        label_visibility="collapsed",
        height=80
    )
    
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    
    if st.button("Generate Detailed Email", key="detailed_generate", disabled=not context.strip()):
        st.session_state.is_processing = True
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Handle processing
if st.session_state.is_processing:
    with st.spinner("Mayowa is writing your email..."):
        time.sleep(1)  # Visual feedback
        
        # Quick generation
        if 'quick_prompt' in st.session_state and st.session_state.quick_prompt.strip():
            result = quick_generate_email(st.session_state.quick_prompt)
            st.session_state.generated_email = result
        
        # Detailed generation
        elif 'context' in st.session_state and st.session_state.context.strip():
            result = generate_email(
                context=st.session_state.context,
                key_points=st.session_state.key_points if st.session_state.key_points else None,
                special_instructions=st.session_state.special_instructions if st.session_state.special_instructions else None,
                urgency=st.session_state.urgency if st.session_state.urgency else "normal"
            )
            st.session_state.generated_email = result
        
        st.session_state.is_processing = False
        st.rerun()

# Output Section
st.markdown('<span class="output-label">Generated Email</span>', unsafe_allow_html=True)

if st.session_state.generated_email:
    st.markdown(f"""
    <div class="output-container">
        <div class="output-text">{st.session_state.generated_email}</div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="output-container">
        <div class="output-placeholder">Your personalized email will appear here...</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>Designed with precision, care and love 🧡.</p>
</div>
""", unsafe_allow_html=True)

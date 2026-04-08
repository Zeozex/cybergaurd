import random
import uuid
import sys
import os

# Ensure the current directory (server/) is in the path
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

    from openenv.core.env_server import Environment
    # These are now imported from the same folder
    from models import CyberGuardAction, CyberGuardObservation, CyberGuardState

    MESSAGES = [

    # ================= SAFE (25) =================

    {"text": "Swiggy Update:\nYour order (#SG92821) has been picked up and is arriving in approx 5 mins.\nPlease share OTP 4432 ONLY after receiving your order. Do NOT share on call.", "type": "sms", "label": "safe", "difficulty": "easy"},

    {"text": "Mom:\nHey, dont forget to pick up the laundry on your way back.\nThey might close early today, so pls try before 8 pm.", "type": "whatsapp", "label": "safe", "difficulty": "easy"},

    {"text": "Jio Alert:\nYou have used 50% of your daily 2GB data pack.\nAfter limit, speed may reduce as per plan.", "type": "sms", "label": "safe", "difficulty": "easy"},

    {"text": "Netflix:\nYour monthly subscription has been successfully renewed.\nEnjoy watching your favorite shows uninterrupted 😊", "type": "email", "label": "safe", "difficulty": "easy"},

    {"text": "Amazon:\nYour package is out for delivery today.\nTracking ID AZ-99812. Track live on amazon.in anytime.", "type": "sms", "label": "safe", "difficulty": "easy"},

    {"text": "Google Security Alert:\nA new login was detected from a Windows device in Bangalore.\nIf this was you, ignore. Otherwise review activity immediately.", "type": "email", "label": "safe", "difficulty": "medium"},

    {"text": "HDFC Bank:\nYour credit card statement for card ending 4452 is generated.\nLogin to NetBanking or mobile app to view & pay dues.", "type": "email", "label": "safe", "difficulty": "medium"},

    {"text": "Zomato:\nHow was your last order from Burger King?\nRate it now & get 10% OFF on your next order 🍔", "type": "whatsapp", "label": "safe", "difficulty": "medium"},

    {"text": "Microsoft:\nYour account password was successfully changed.\nIf this wasn't you, please secure your account immediately.", "type": "email", "label": "safe", "difficulty": "medium"},

    {"text": "Airtel:\nRecharge of ₹719 completed successfully.\nPlan valid till 15-Jun-2026. Enjoy uninterrupted service.", "type": "sms", "label": "safe", "difficulty": "medium"},

    {"text": "OTP Alert:\nYour Aadhaar verification OTP is 992813.\nDo NOT share this code with anyone under any condition.", "type": "sms", "label": "safe", "difficulty": "hard"},

    {"text": "IRCTC:\nYour ticket for Train 12951 is confirmed.\nCoach B2, Seat 44. Have a pleasant journey 🚆", "type": "sms", "label": "safe", "difficulty": "hard"},

    {"text": "LinkedIn:\n5 people viewed your profile this week.\nCheck insights to see who is interested in your profile.", "type": "email", "label": "safe", "difficulty": "hard"},

    {"text": "Apple:\niCloud storage is 90% full.\nUpgrade plan to avoid backup interruptions.", "type": "email", "label": "safe", "difficulty": "hard"},

    {"text": "Uber:\nYour ride with driver Amit has arrived.\nVerify trip using PIN 1022 before starting.", "type": "sms", "label": "safe", "difficulty": "hard"},

    {"text": "Society Notice:\nWater supply will be interrupted tomorrow.\nTiming: 10 AM to 2 PM. Please store water in advance.", "type": "whatsapp", "label": "safe", "difficulty": "easy"},

    {"text": "Spotify:\nTry Premium Family free for 1 month.\nEnjoy ad-free music experience 🎧", "type": "email", "label": "safe", "difficulty": "easy"},

    {"text": "Paytm:\nYou received ₹10 cashback for your last payment.\nCheck your wallet for updated balance.", "type": "sms", "label": "safe", "difficulty": "medium"},

    {"text": "IndiGo:\nOnline check-in is now open for flight 6E-502.\nComplete early to avoid airport delays.", "type": "sms", "label": "safe", "difficulty": "hard"},

    {"text": "GitHub:\nA new personal access token was created.\nIf not you, revoke it immediately from settings.", "type": "email", "label": "safe", "difficulty": "hard"},

    {"text": "Tata Sky:\nYour account balance is low.\nRecharge soon to continue uninterrupted viewing.", "type": "sms", "label": "safe", "difficulty": "easy"},

    {"text": "Clinic Reminder:\nYour appointment is confirmed for tomorrow at 5:30 PM.\nPlease arrive 10 mins early for check-in.", "type": "sms", "label": "safe", "difficulty": "medium"},

    {"text": "Discord:\nWelcome to OpenEnv Hackathon server!\nPlease read rules & introduce yourself 👋", "type": "email", "label": "safe", "difficulty": "easy"},

    {"text": "ICICI Bank:\n₹50,000 credited via NEFT.\nCheck updated balance in iMobile app.", "type": "sms", "label": "safe", "difficulty": "hard"},

    {"text": "YouTube:\nTechDaily uploaded a new video.\nWatch now: Best AI Tools 2026 🚀", "type": "email", "label": "safe", "difficulty": "easy"},


    # ================= SUSPICIOUS (25) =================

    {"text": "Reminder:\nYour electricity bill is pending.\nPlease clear dues today to avoid inconvenience.", "type": "sms", "label": "suspicious", "difficulty": "easy"},

    {"text": "Hi there 👋\nWe found your resume online.\nPart-time job available earning ₹20k/week. Interested?", "type": "whatsapp", "label": "suspicious", "difficulty": "easy"},

    {"text": "Refund Notice:\nYou have ₹2,500 pending refund.\nClick here to verify your details: tinyurl.com/refund", "type": "sms", "label": "suspicious", "difficulty": "easy"},

    {"text": "Amazon Alert:\nYour account has been locked due to unusual login.\nVerify identity at login-amazon-help.com", "type": "email", "label": "suspicious", "difficulty": "medium"},

    {"text": "Congrats 🎉\nYou are selected in lucky draw.\nCall now to claim reward before expiry.", "type": "whatsapp", "label": "suspicious", "difficulty": "medium"},

    {"text": "Tax Dept:\nError detected in your filing.\nDownload report to resolve immediately.", "type": "email", "label": "suspicious", "difficulty": "medium"},

    {"text": "Parcel Notice:\nYour package is held at customs.\nPay small handling fee to release it.", "type": "sms", "label": "suspicious", "difficulty": "medium"},

    {"text": "Security Alert:\nLogin detected from Nigeria.\nIf not you, secure account immediately.", "type": "email", "label": "suspicious", "difficulty": "medium"},

    {"text": "Hey it's me...\nLost my phone 😭\nSend pics from yesterday here pls urgent", "type": "whatsapp", "label": "suspicious", "difficulty": "hard"},

    {"text": "Earn Money Fast 💸\nLike videos & earn ₹50k/month.\nJoin Telegram now to start.", "type": "whatsapp", "label": "suspicious", "difficulty": "hard"},

    {"text": "Bank Notice:\nWe are updating systems.\nPlease confirm your phone number for verification.", "type": "sms", "label": "suspicious", "difficulty": "hard"},

    {"text": "Flash Sale ⚡\niPhone 15 at 90% OFF.\nOffer valid for next 10 minutes only.", "type": "email", "label": "suspicious", "difficulty": "easy"},

    {"text": "Subscription Alert:\nYour plan will auto-renew for $499.\nCall support if you want to cancel.", "type": "email", "label": "suspicious", "difficulty": "medium"},

    {"text": "Insurance Notice:\nYour policy is about to expire.\nUpdate bank details to continue coverage.", "type": "sms", "label": "suspicious", "difficulty": "medium"},

    {"text": "Crypto Offer:\nFree giveaway for first 100 users.\nRegister now to claim BTC reward.", "type": "sms", "label": "suspicious", "difficulty": "easy"},

    {"text": "Credit Alert:\nYour credit score dropped significantly.\nCheck reason at this link.", "type": "sms", "label": "suspicious", "difficulty": "hard"},

    {"text": "Private Content:\nA friend shared a video with you.\nLogin to view securely.", "type": "email", "label": "suspicious", "difficulty": "medium"},

    {"text": "Post Office:\nPackage delivery failed.\nUpdate address to reschedule delivery.", "type": "sms", "label": "suspicious", "difficulty": "hard"},

    {"text": "Domain Alert:\nYour domain expires in 24 hrs.\nRenew now to avoid loss.", "type": "email", "label": "suspicious", "difficulty": "medium"},

    {"text": "Win Trip ✈️\nTrip to Dubai awaits you.\nFill survey to participate.", "type": "whatsapp", "label": "suspicious", "difficulty": "easy"},

    {"text": "Car Insurance:\nPremium overdue.\nPay now to avoid legal penalty.", "type": "sms", "label": "suspicious", "difficulty": "medium"},

    {"text": "System Alert:\nVirus detected on your computer.\nDownload scanner to remove threats.", "type": "email", "label": "suspicious", "difficulty": "easy"},

    {"text": "Customer Support:\nNeed to verify your address.\nReply with details for shipment.", "type": "whatsapp", "label": "suspicious", "difficulty": "medium"},

    {"text": "Investment Plan:\nDouble your money in 3 months.\nLimited AI trading slots available.", "type": "sms", "label": "suspicious", "difficulty": "hard"},

    {"text": "Email Notice:\nConfirm your email to keep account active.\nFailure may result in suspension.", "type": "email", "label": "suspicious", "difficulty": "hard"},


    # ================= HIGHLY SUSPICIOUS (25) =================

    {"text": "HDFC ALERT ⚠️\nNetBanking deactivated due to KYC issue.\nUpdate NOW at bit.ly/hdfc-update or account blocked.", "type": "sms", "label": "highly_suspicious", "difficulty": "easy"},

    {"text": "IRS Notice:\nRefund of $1450 pending.\nSubmit SSN + bank details to claim.", "type": "email", "label": "highly_suspicious", "difficulty": "easy"},

    {"text": "URGENT ⚠️\nYour Apple ID under investigation.\nVerify within 24 hrs or account deleted.", "type": "email", "label": "highly_suspicious", "difficulty": "medium"},

    {"text": "WhatsApp Notice:\nAccount will be deleted soon.\nVerify identity NOW to continue.", "type": "whatsapp", "label": "highly_suspicious", "difficulty": "medium"},

    {"text": "SBI Alert:\nYONO account blocked.\nUpdate PAN at sbi-yono-verification.in immediately.", "type": "sms", "label": "highly_suspicious", "difficulty": "medium"},

    {"text": "PayPal Notice:\nAccount limited due to unusual activity.\nDownload attached form to resolve.", "type": "email", "label": "highly_suspicious", "difficulty": "medium"},

    {"text": "Govt Alert:\nEligible for relief fund.\nRegister now to claim benefits.", "type": "sms", "label": "highly_suspicious", "difficulty": "hard"},

    {"text": "Security Warning:\nPassword compromised.\nVerify identity at google-security-check.co", "type": "email", "label": "highly_suspicious", "difficulty": "hard"},

    {"text": "Bank Alert:\nLoan request ₹10L initiated.\nCancel immediately if not you.", "type": "sms", "label": "highly_suspicious", "difficulty": "hard"},

    {"text": "Facebook:\nAccount will be disabled.\nAppeal using link provided.", "type": "email", "label": "highly_suspicious", "difficulty": "medium"},

    {"text": "Coinbase:\nUnusual login detected.\nVerify account to unlock withdrawals.", "type": "sms", "label": "highly_suspicious", "difficulty": "medium"},

    {"text": "Emergency:\nYour child in accident 😰\nSend ₹5000 urgently for treatment.", "type": "whatsapp", "label": "highly_suspicious", "difficulty": "easy"},

    {"text": "Microsoft Support:\nWindows license expired.\nCall support immediately to renew.", "type": "email", "label": "highly_suspicious", "difficulty": "easy"},

    {"text": "Netflix:\nPayment failed.\nAccount will cancel in 12 hrs.", "type": "email", "label": "highly_suspicious", "difficulty": "medium"},

    {"text": "Card Alert:\n$1200 spent at GUCCI.\nCall now if unauthorized.", "type": "sms", "label": "highly_suspicious", "difficulty": "hard"},

    {"text": "Police Notice:\nUnpaid fine detected.\nPay immediately or warrant issued.", "type": "sms", "label": "highly_suspicious", "difficulty": "medium"},

    {"text": "Gas Service:\nConnection will be cut tonight.\nComplete KYC immediately.", "type": "sms", "label": "highly_suspicious", "difficulty": "easy"},

    {"text": "Yahoo:\nAccount deletion requested.\nClick to cancel action.", "type": "email", "label": "highly_suspicious", "difficulty": "hard"},

    {"text": "Binance:\nNew login detected.\nReset password if not you.", "type": "email", "label": "highly_suspicious", "difficulty": "medium"},

    {"text": "COVID Relief:\nClaim ₹5000 subsidy.\nApply at government portal now.", "type": "sms", "label": "highly_suspicious", "difficulty": "medium"},

    {"text": "Tinder:\nAccount reported.\nVerify now to avoid ban.", "type": "email", "label": "highly_suspicious", "difficulty": "hard"},

    {"text": "Marriott:\nFree stay offer 🎉\nPay small tax to confirm booking.", "type": "whatsapp", "label": "highly_suspicious", "difficulty": "easy"},

    {"text": "Bitwarden:\nVault accessed from new device.\nCheck activity immediately.", "type": "email", "label": "highly_suspicious", "difficulty": "hard"},

    {"text": "PAN Alert:\nNot linked with bank.\nUpdate now to avoid freeze.", "type": "sms", "label": "highly_suspicious", "difficulty": "medium"},

    {"text": "Security Alert:\nCamera system accessed remotely.\nCheck immediately for safety.", "type": "email", "label": "highly_suspicious", "difficulty": "hard"},


    # ================= SCAM (25) =================

    {"text": "CONGRATS!!! 🎉\nYou won $1,000,000 Coca-Cola lottery.\nEmail win@scam.com to claim NOW.", "type": "email", "label": "scam", "difficulty": "easy"},

    {"text": "URGENT 🚨\nYour bank account drained!!\nCall 1800-SCAM-NOW immediately.", "type": "sms", "label": "scam", "difficulty": "easy"},

    {"text": "Hello Dear,\nI am a prince with $50M.\nHelp transfer & you get 10%.", "type": "email", "label": "scam", "difficulty": "easy"},

    {"text": "Warning ⚠️\nYour phone infected with viruses.\nClick here to clean NOW.", "type": "sms", "label": "scam", "difficulty": "easy"},

    {"text": "Get Rich 💰\nInvest $100 → $1000 in 24hrs.\nGuaranteed return, act fast!", "type": "whatsapp", "label": "scam", "difficulty": "easy"},

    {"text": "Amazon Gift:\nSelected for free reward.\nPay $1 shipping to receive.", "type": "email", "label": "scam", "difficulty": "medium"},

    {"text": "Hi,\nThis is your CEO.\nBuy $500 gift cards urgently.", "type": "whatsapp", "label": "scam", "difficulty": "medium"},

    {"text": "Netflix Alert:\nAccount suspended.\nUpdate billing at fake link.", "type": "email", "label": "scam", "difficulty": "medium"},

    {"text": "Electricity Notice:\nPower cut in 1 hr.\nPay technician via UPI NOW.", "type": "whatsapp", "label": "scam", "difficulty": "medium"},

    {"text": "Job Offer:\nSelected for Amazon role.\nPay ₹500 to proceed onboarding.", "type": "whatsapp", "label": "scam", "difficulty": "easy"},

    {"text": "Security Alert:\nSSN used in crime.\nCall immediately to resolve.", "type": "sms", "label": "scam", "difficulty": "medium"},

    {"text": "Google Job:\nOffer confirmed.\nPay laptop shipping fee $200.", "type": "email", "label": "scam", "difficulty": "medium"},

    {"text": "Apple Alert:\nPurchase of $99 detected.\nCancel via this link.", "type": "email", "label": "scam", "difficulty": "hard"},

    {"text": "Tech Support:\nYour PC infected.\nCall +1-FAKE-TECH immediately.", "type": "email", "label": "scam", "difficulty": "easy"},

    {"text": "Instagram:\nAccount deletion in 24h.\nAppeal at fake site.", "type": "email", "label": "scam", "difficulty": "hard"},

    {"text": "Loan Offer:\n₹5L instant loan.\nApply now no documents.", "type": "sms", "label": "scam", "difficulty": "easy"},

    {"text": "Electricity:\nCutoff soon.\nPay Raj via UPI immediately.", "type": "whatsapp", "label": "scam", "difficulty": "medium"},

    {"text": "Facebook:\nSuspicious login.\nSecure account at fake link.", "type": "email", "label": "scam", "difficulty": "hard"},

    {"text": "DHL:\nParcel pending.\nPay customs fee online.", "type": "sms", "label": "scam", "difficulty": "hard"},

    {"text": "HR Notice:\nSalary hike letter ready.\nClick to download.", "type": "email", "label": "scam", "difficulty": "hard"},

    {"text": "Rewards:\nPoints expiring.\nRedeem for free iPhone.", "type": "sms", "label": "scam", "difficulty": "medium"},

    {"text": "Binance:\nWithdrawal in progress.\nCancel using fake link.", "type": "email", "label": "scam", "difficulty": "hard"},

    {"text": "Tesla Giveaway:\nWin a free Tesla.\nEnter using this link.", "type": "whatsapp", "label": "scam", "difficulty": "easy"},

    {"text": "Amazon Prime:\nMembership cancelled.\nReactivate via fake site.", "type": "email", "label": "scam", "difficulty": "medium"},

    {"text": "SBI KYC:\nExpired.\nUpdate now or account closed.", "type": "sms", "label": "scam", "difficulty": "medium"},

    {"text": "Job Alert:\nShortlisted for Amazon.\nPay registration fee now.", "type": "whatsapp", "label": "scam", "difficulty": "easy"}

    ]

    class CyberGuardEnvironment(Environment):
        def __init__(self):
                self._state = CyberGuardState()
                        self._current_message = None
                                self._messages = MESSAGES.copy()
                                        self._last_reward = 0.0
                                                random.shuffle(self._messages)
                                                        self._index = 0

                                                            def reset(self) -> CyberGuardObservation:
                                                                    self._state = CyberGuardState()
                                                                            self._messages = MESSAGES.copy()
                                                                                    self._last_reward = 0.0
                                                                                            random.shuffle(self._messages)
                                                                                                    self._index = 0
                                                                                                            self._state.episode_id = str(uuid.uuid4())
                                                                                                                    self._current_message = self._messages[self._index]
                                                                                                                            
                                                                                                                                    return CyberGuardObservation(
                                                                                                                                                message=self._current_message["text"],
                                                                                                                                                            message_type=self._current_message["type"],
                                                                                                                                                                        difficulty=self._current_message["difficulty"],
                                                                                                                                                                                    done=False,
                                                                                                                                                                                                reward=0.0
                                                                                                                                                                                                        )

                                                                                                                                                                                                            def step(self, action: CyberGuardAction) -> CyberGuardObservation:
                                                                                                                                                                                                                    if self._current_message is None:
                                                                                                                                                                                                                                return self.reset()

                                                                                                                                                                                                                                        correct_label = self._current_message["label"]
                                                                                                                                                                                                                                                difficulty = self._current_message["difficulty"]
                                                                                                                                                                                                                                                        ai_label = action.label

                                                                                                                                                                                                                                                                # Scoring logic with standard hackathon reward range (0.0 to 1.0)
                                                                                                                                                                                                                                                                        label_order = ["safe", "suspicious", "highly_suspicious", "scam"]
                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                        if ai_label == correct_label:
                                                                                                                                                                                                                                                                                                    if difficulty == "easy":
                                                                                                                                                                                                                                                                                                                    reward = 0.5
                                                                                                                                                                                                                                                                                                                                elif difficulty == "medium":
                                                                                                                                                                                                                                                                                                                                                reward = 0.7
                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                            reward = 1.0
                                                                                                                                                                                                                                                                                                                                                                                    elif abs(label_order.index(ai_label) - label_order.index(correct_label)) == 1:
                                                                                                                                                                                                                                                                                                                                                                                                reward = 0.2 
                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                    reward = 0.0 # No penalty below 0 to stay in safe 0-1 range

                                                                                                                                                                                                                                                                                                                                                                                                                            self._last_reward = reward
                                                                                                                                                                                                                                                                                                                                                                                                                                    self._state.step_count += 1
                                                                                                                                                                                                                                                                                                                                                                                                                                            self._state.current_score += reward

                                                                                                                                                                                                                                                                                                                                                                                                                                                    self._index += 1
                                                                                                                                                                                                                                                                                                                                                                                                                                                            done = self._index >= len(self._messages)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if not done:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                self._current_message = self._messages[self._index]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            return CyberGuardObservation(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            message=self._current_message["text"],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            message_type=self._current_message["type"],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            difficulty=self._current_message["difficulty"],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            done=False,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            reward=float(reward)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        )
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            self._current_message = None
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        return CyberGuardObservation(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        message="End of evaluation.",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        message_type="n/a",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        difficulty="n/a",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        done=True,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        reward=float(reward)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    )

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        @property
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            def state(self) -> CyberGuardState:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    return self._state
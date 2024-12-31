from django.db import models
from Main.models import User, Appointment

# Models that inherit this, will have the below attributes/methods in common
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Assessment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hijama_assessments_user')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='hijama_assessments_appointment', null=True, blank=True)

    ##### Personal info: #####
    name = models.CharField(max_length=100, verbose_name="নাম/Name")
    age = models.IntegerField(verbose_name="বয়স/Age") 
    # Integer for gender 
    MALE = 1
    FEMALE = 0
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.IntegerField(choices=GENDER_CHOICES, verbose_name="লিঙ্গ/Gender")
    address = models.TextField(verbose_name="ঠিকানা/Address")


    ##### Medical info: #####
    # Integer for diabetes level
    HIGH = 1
    NORMAL = 0
    LOW = -1
    UNAWARE = -1
    DIABETES_CHOICES = [
        (HIGH, 'High'),
        (NORMAL, 'Normal'),
        (LOW, 'Low'),
        (UNAWARE, 'Unaware'),
    ]
    diabetes = models.IntegerField(choices=DIABETES_CHOICES, verbose_name="ডায়াবেটিস(খালিপেটে)/Diabetes(Empty stomach)")
    # Integer for blood pressure 
    HIGH = 1
    NORMAL = 0
    LOW = -1
    UNAWARE = -1
    BLOOD_PRESSURE_CHOICES = [
        (HIGH, 'High'),
        (NORMAL, 'Normal'),
        (LOW, 'Low'),
        (UNAWARE, 'Unaware'),
    ]
    blood_pressure = models.IntegerField(choices=BLOOD_PRESSURE_CHOICES, verbose_name="রক্তচাপ/Blood Pressure") 
    is_recent_surgery = models.BooleanField(default=False, verbose_name="সাম্প্রতিক কোনো সার্জারি/Any recent surgery")
    is_wounds_take_time = models.BooleanField(default=False, verbose_name="কাটা বা ঘা শুকাতে সময় লাগে/Cuts or wounds take time to heal")
    is_hemophilia = models.BooleanField(default=False, verbose_name="হিমোফিলিয়া-এ এবং বি অথবা প্লাটিলেট কাউন্ট কম/হemophilia A and B or low platelet count")
    is_excessive_blood_problems = models.BooleanField(default=False, verbose_name="অত্যধিক রক্তপাত সমস্যা/Excessive bleeding problems")
    is_anemia = models.BooleanField(default=False, verbose_name="রক্ত শুন্যতা বা অ্যানিমিয়া/Anemia") 
    is_fainting_attacks = models.BooleanField(default=False, verbose_name="ঘন ঘন অজ্ঞান বা বেহুশ হওয়া/Fainting attacks") 
    is_black_out = models.BooleanField(default=False, verbose_name="ব্ল্যাক আউট/Blackouts") 
    is_epilepsy = models.BooleanField(default=False, verbose_name="মৃগীরোগ/Epilepsy") 
    is_liver_desease = models.BooleanField(default=False, verbose_name="লিভারে সমস্যা/Liver Disease") 
    is_kidney_desease = models.BooleanField(default=False, verbose_name="কিডনী রোগ/Kidney Disease") 
    is_cardiac_desease = models.BooleanField(default=False, verbose_name="হৃদরোগ/Heart or Cardiac Disease") 
    is_lung_desease = models.BooleanField(default=False, verbose_name="ফুসফুসে অসুস্থতা/Lung Disease") 
    is_brain_stroke = models.BooleanField(default=False, verbose_name="ব্রেন স্ট্রোক/Brain stroke") 
    is_blood_thinners = models.BooleanField(default=False, verbose_name="রক্ত পাতলা করার ওষুধ বা ইঞ্জেকশন নেন(যেমন-এসপ্রিন,ওয়ারফেরিন, হেপারিন ইত্যাদি)/Take any blood thinner medicine or injection(For example- Aspirin, Warfarin, Heparin etc)") 
    is_migraine = models.BooleanField(default=False, verbose_name="মাইগ্রেন/Migraine") 
    is_headache = models.BooleanField(default=False, verbose_name="মাথাব্যথা/Headache") 
    is_back_pain = models.BooleanField(default=False, verbose_name="পিঠ পেইন/Back Pain") 
    is_lower_back_pain = models.BooleanField(default=False, verbose_name="কোমর ব্যথা/Lower Back Pain") 
    is_leg_pain = models.BooleanField(default=False, verbose_name="পায়ে ব্যাথা/Leg Pain") 
    is_shoulder_pain = models.BooleanField(default=False, verbose_name="কাধে ব্যথা/Shoulder Pain") 
    is_elbow_pain = models.BooleanField(default=False, verbose_name="কনুইয়ে ব্যথা/Elbow Pain") 
    is_knee_pain = models.BooleanField(default=False, verbose_name="হাঁটু ব্যথা/Knee Pain") 
    is_wrist_pain = models.BooleanField(default=False, verbose_name="কব্জিতে ব্যথা/Wrist Pain") 
    is_hip_pain = models.BooleanField(default=False, verbose_name="নিতম্বে ব্যথা/Hip Pain") 
    is_ankle_pain = models.BooleanField(default=False, verbose_name="গোড়ালিতে ব্যথা/Ankle Pain") 
    is_fracture_pain = models.BooleanField(default=False, verbose_name="হাড়ের স্থানচ্যুতি জনিত ব্যথা/Fracture Pain") 
    is_gout_pain = models.BooleanField(default=False, verbose_name="জয়েন্টের ব্যথা/Gout Pain") 
    is_heel_pain = models.BooleanField(default=False, verbose_name="পায়ের তালুতে ব্যথা/Heel Pain") 
    is_muscles_pain = models.BooleanField(default=False, verbose_name="মাংসপেশীর ব্যাথা/Muscles Strain") 
    is_arthritis = models.BooleanField(default=False, verbose_name="গেটে বাত বা আর্থ্রাইটিস/Arthritis or Rheumatism") 
    is_osteoporosis = models.BooleanField(default=False, verbose_name="হাড়ের ক্ষয় রোগ/Osteoporosis") 
    is_cancer_pain = models.BooleanField(default=False, verbose_name="ক্যনসারের ব্যথা/Cancer pain") 
    
    ##### Only for women: #####
    is_infertile = models.BooleanField(default=False, verbose_name="বন্ধ্যাত্ব/Infertility") 
    is_ovarian_cysts = models.BooleanField(default=False, verbose_name="ওভারিয়ান সিস্ট/Ovarian Cysts") 
    is_uterus_problem = models.BooleanField(default=False, verbose_name="জরায়ূ বা গর্ভাশয়ে সমস্যা/Uterus Problem") 
    is_excess_bleeding = models.BooleanField(default=False, verbose_name="অতিরিক্ত রক্তপাত/Excess Bleeding") 
    is_amenorrhea = models.BooleanField(default=False, verbose_name="এমেনোরিয়া(মাসিক বন্ধ)/Amenorrhea") 
    is_sadistic = models.BooleanField(default=False, verbose_name="সাদাস্রাব/Sadistic") 
    is_menstrual_problem = models.BooleanField(default=False, verbose_name="মাসিকের সমস্যা/Menstrual Problems") 
    is_irregular_menses = models.BooleanField(default=False, verbose_name="অনিয়মিত মাসিক/Irregular Manses") 
    is_ovary_problem = models.BooleanField(default=False, verbose_name="ডিম্বাশয়ের সমস্যা/Ovary Problems") 

    ##### Only for men: #####
    is_sexual_dysfunction = models.BooleanField(default=False, verbose_name="যৌন রোগ/Sexual Dysfunction") 
    is_erectile_dysfunction = models.BooleanField(default=False, verbose_name="ইরেকটাইল ডিসফাংশন বা ইরেকশন ফেইলিউর: পুরুষ লিঙ্গের উত্থানে ব্যর্থতা/Erectile Dysfunction (ED) or erection failure: Failure of the male penis to erect") 
    is_penetration_failure = models.BooleanField(default=False, verbose_name="পোনিট্রেশন ফেইলিউর: লিঙ্গের যোনিদ্বার ছেদনে ব্যর্থতা/Penetration Failure: Failure of the penis to penetrate the vagina") 
    is_premature_ejaculation = models.BooleanField(default=False, verbose_name="প্রি-ম্যাচুর ইজাকুলেশন: সহবাসে দ্রুত বীর্যস্খলন তথা স্থায়ীত্বের অভাব/Premature Ejaculation: Rapid ejaculation or lack of permanence during intercourse") 


    ##### Paranormal: #####
    is_jinn_affliction = models.BooleanField(default=False, verbose_name="জ্বীনের নিপীড়ন/Jinn Affliction") 
    is_black_magic = models.BooleanField(default=False, verbose_name="কালো যাদু/Black Magic") 
    is_waswas = models.BooleanField(default=False, verbose_name="ওয়াসওয়াস/Waswas (Whisperings/OCD)") 
    

    ##### Miscellaneous: #####
    is_asthma = models.BooleanField(default=False, verbose_name="শ্বাস কষ্ট(হাঁপানি বা এস্থেমা)/Breathing difficulty(Asthma)") 
    is_eczema = models.BooleanField(default=False, verbose_name="একজিমা/Eczema") 
    is_hey_fever = models.BooleanField(default=False, verbose_name="হেই ফিভার/Hay fever") 
    is_hepatitis = models.BooleanField(default=False, verbose_name="জন্ডিস বা হেপাটাইটিস(বি বা সি)/Hepatitis(B or C)") 
    is_bronchitis = models.BooleanField(default=False, verbose_name="ব্রনক্রাইটিস/Bronchitis") 
    is_psoriasis = models.BooleanField(default=False, verbose_name="সরাইসিস/Psoriasis") 
    is_allergies = models.BooleanField(default=False, verbose_name="এলার্জি/Allergies") 
    is_thyroid = models.BooleanField(default=False, verbose_name="থাইরয়েড সমস্যা/Thyroid Problem") 
    is_sports_injury = models.BooleanField(default=False, verbose_name="স্পোর্টস ইনজুরি/Sports Injury") 
    is_skin_disease = models.BooleanField(default=False, verbose_name="দীর্ঘমেয়াদী চর্মরোগ/Chronic Skin Diseases") 
    is_boil = models.BooleanField(default=False, verbose_name="ফোঁড়া/Boil") 
    is_scabies = models.BooleanField(default=False, verbose_name="পাঁচড়া বা চুলকানি/Scabies") 
    is_blood_purification = models.BooleanField(default=False, verbose_name="রক্ত পরিস্কারকরণ/Blood purification") 
    is_sinuses_problem = models.BooleanField(default=False, verbose_name="সাইনুসাইটিস/Sinuses Problem") 
    is_psychological_disorder = models.BooleanField(default=False, verbose_name="মানসিক সমস্যা/Psychological Disorder") 
    is_disc_prolapse = models.BooleanField(default=False, verbose_name="ডিস্ক প্রলেপস/Disc Prolapse") 
    is_stomach_problem = models.BooleanField(default=False, verbose_name="পাকস্থলীর সমস্যা/Stomach Problems") 
    is_varicose_vein = models.BooleanField(default=False, verbose_name="ভ্যারিকোস ভেইন/Varicose Vein") 
    is_detoxification = models.BooleanField(default=False, verbose_name="শরীরের বর্জ্য নিস্কাশন/Detoxification") 
    is_ear_problem = models.BooleanField(default=False, verbose_name="কানের সমস্যা/Ear Problems") 
    is_dizziness = models.BooleanField(default=False, verbose_name="মাথা ঘোরা/Dizziness") 
    is_prostate_enlarge = models.BooleanField(default=False, verbose_name="প্রসট্রেইট বড় হওয়া/Prostate Enlarge") 
    is_tmd = models.BooleanField(default=False, verbose_name="প্টেম্পোরোম্যান্ডিবুলার জয়েন্ট ডিসফাংশন(টিএমডি বা টিএমজে)/Temporomandibular joint dysfunction(TMD or TMJ)") 
    is_uric_acid = models.BooleanField(default=False, verbose_name="ইউরিক এসিড/Uric acid") 
    is_insomnia = models.BooleanField(default=False, verbose_name="ঘুমের ব্যাঘাত বা অনিদ্রা/Insomnia") 
    is_forgetting = models.BooleanField(default=False, verbose_name="ষ্মৃতিভ্রষ্টতা/Forgetting") 
    is_poor_memory = models.BooleanField(default=False, verbose_name="দুর্বল স্মৃতি শক্তি/Poor Memory") 
    is_drug_addiction = models.BooleanField(default=False, verbose_name="মাদকাসক্তি/Drug Addiction") 
    is_ibs = models.BooleanField(default=False, verbose_name="ইরিটেবল বাওয়েল সিনড্রম (IBS)") 
    is_laziness = models.BooleanField(default=False, verbose_name="অলসতা/Laziness") 
    is_underweight = models.BooleanField(default=False, verbose_name="আন্ডার ওয়েট/Underweight") 
    is_parkinson = models.BooleanField(default=False, verbose_name="স্নায়বিক রোগ/Parkinson's Disease") 
    is_brain_disorder = models.BooleanField(default=False, verbose_name="মস্তিস্কের রোগ/Brain Disorder") 
    is_bron = models.BooleanField(default=False, verbose_name="মুখে ব্রন/Bron in the face") 
    is_depression = models.BooleanField(default=False, verbose_name="বিষন্নতা/Depression") 
    is_hormonal_imbalance = models.BooleanField(default=False, verbose_name="হরমোনের সমস্যা/Hormonal Imbalance") 
    is_piles = models.BooleanField(default=False, verbose_name="অর্শ/Piles") 
    is_fistula = models.BooleanField(default=False, verbose_name="ভগন্দর/Fistula") 
    is_anal_fissure = models.BooleanField(default=False, verbose_name="পোঁদ ফাটল/Anal Fissure") 
    is_paralysis = models.BooleanField(default=False, verbose_name="অবশাঙ্গতা/Paralysis") 
    is_low_immunity = models.BooleanField(default=False, verbose_name="রোগ প্রতিরোধ ক্ষমতা কম/Low Immunity") 
    is_hair_loss = models.BooleanField(default=False, verbose_name="চুল পড়া/ Hair loss") 

    current_treatment_details = models.TextField(verbose_name="আপনি কি কোন ডাক্তার, স্বাস্থ্যসেবা প্রদানকারীর চিকিৎসা সেবা নিয়েছেন? আপনি কি কোন ধরণের চিকিৎসাধীন আছেন? বিস্তারিত প্রদান বর্ণনা করুন:Have you been diagnosed by a professional doctor, health care provider? Are you under a medical treatment plan? Please provide details:")
    previous_treatment_details = models.TextField(verbose_name="পূর্ববর্তী চিকিৎসার বিবরণ/Details of previous treatment: ")

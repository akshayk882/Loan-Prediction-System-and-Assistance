from django.shortcuts import render,redirect
from . import classification_d

# Create your views here.
def recommend(loan_amount):
    onelakh=["IDFC Bank","Federal Bank","Punjab and Sind Bank","DCB Bank","Bandhan Bank"]
    fivelakh=["Kotak Mahindra Bank","Indusland Bank","UCO Bank","Bank of Maharashtra","Central Bank of India"]
    tenlakh=["Bank of India","Indian Bank","Union Bank of India","Axis Bank","IDBI Bank"]
    fiftylakh=["ICICI Bank","Canara Bank","HDFC Bank","State Bank of India","Bank of Baroda"]

    if loan_amount >= 100000 and loan_amount < 500000:
        return onelakh

    elif loan_amount >= 500000 and loan_amount < 1000000:
        return onelakh,fivelakh

    elif loan_amount >= 1000000 and loan_amount < 5000000:
        return onelakh,fivelakh,tenlakh

    elif loan_amount >= 5000000:
        return onelakh,fivelakh,tenlakh,fiftylakh

def index(request):
    return render(request,'index.html')

def news(request):
    return render(request,'news.html')

def elements(request):
    return render(request,'elements.html')

def contact(request):
    return render(request,'contact.html')

def about_us(request):
    return render(request,'about-us.html')

def loans(request):
    return render(request,'loans.html')

def details(request):
    if request.user.is_authenticated:
        return render(request,'details.html')
    else:
        return redirect('/../accounts/register')

def predict(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        credit = request.POST.get('credit-history',False)
        education =request.POST.get('education',False)
        employed = request.POST.get("employed", "Guest (or whatever)")
        app_income = int(request.POST['Applicant-income'])
        co_income = int(request.POST['Co-Applicant-income'])
        dependents = request.POST.get('dependents',False)
        loan_amount = int(request.POST['loan-amount'])
        loan_tenure = int(request.POST['loan-tenure'])
        temp_property = request.POST.get('property',False)
        gender = request.POST.get('gender',False)
        
        if temp_property == 'Rural':
            app_property = 0
        elif temp_property == 'Semi Urban':
            app_property = 1
        else:
            app_property = 2
        print(credit)
        if credit == "700 or below":
            credit_history = 0
        else:
            credit_history = 1
        pred_income = int(app_income/70)
        pred_co = int(co_income/70)
        pred_loan = int(loan_amount/70000)
        
        lst = [[pred_income,pred_co,pred_loan,loan_tenure,credit_history,app_property]]
        predict_op = classification_d.decision_tree_predict_loan(lst)


        attr = {"Gender":gender,"Phone":phone,"Education":education,"Dependents":dependents,
                "Employed":employed,"Appliacnt income":app_income,"Co Applicant income":co_income,
                "Loan Amount":loan_amount,"Loan Tenure":loan_tenure,"Credit":credit,
                "Property":app_property}        
        print(predict_op)
        predict_op = predict_op[0]
        if predict_op ==1 :
            pr = "Approved"
            result = "Congratulations!"
        else:
            pr = "Refused"
            result = "We're Sorry!"
       
        if predict_op == 1:
            banks=recommend(loan_amount)
            return render(request,'prediction.html',{'prediction':pr, 
                    "Gender":gender, "phone":phone,"Education":education,"Dependents":dependents,
                    "Employed":employed,"Applicant_income":app_income,"Co_Applicant_income":co_income,
                    "Loan_Amount":loan_amount,"Loan_Tenure":loan_tenure,"Credit":credit,
                    "Property":temp_property, "result":result, "Banks":banks})
        else:
            new_interest = 0
            new_prediction = predict_op
            new_lst = [[pred_income,pred_co,pred_loan,loan_tenure,credit_history,app_property]]
            while new_prediction ==0 :
                new_interest += 0.2*pred_income
                new_income= new_interest*5
                new_lst[0][0] = new_income
                new_prediction = classification_d.decision_tree_predict_loan(new_lst)
                new_prediction = new_prediction[0]
            new_interest = new_interest*70
            required_saving = new_interest/app_income*100
            print(new_interest)
            return render(request,'prediction.html',{'prediction':pr, 
                    "Gender":gender, "phone":phone,"Education":education,"Dependents":dependents,
                    "Employed":employed,"Applicant_income":app_income,"Co_Applicant_income":co_income,
                    "Loan_Amount":loan_amount,"Loan_Tenure":loan_tenure,"Credit":credit,
                    "Property":temp_property, "result":result,"Saving":required_saving})
    else:
        return redirect('details')

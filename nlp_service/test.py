from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# The JSON data
json_data = [
    {
        "q": "What Happens When Term Life Insurance Ends?",
        "a": "\"One of two things happens at the end of the term of term life insurance depending on the contract. One is the policy simply cancels and nothing else will happen. Second are more common is you will experience a steep premium increase usually 7 to 10 times the price. Some policies allow you to convert to a permanent whole life plan but could be expensive or you can just purchase another term life insurance plan assuming your health is still OK."
    },
    {
        "q": "What Happens When Term Life Insurance Expires?",
        "a": "\"When term life insurance expires death benefit coverage is over. Some term life insurance companies offer a 60 day reinstatement period for you to reconsider term conversion if the provision is available through the entire term of the contract. Its best to convert and secure other cover if the original reason for the existing coverage still remains."
    },
    {
        "q": "What Happens When A Term Life Insurance Term Ends?",
        "a": "\"Most term insurance policies increase dramatically in price after the level term period and clients simply stop paying for them and they lapse. Many term policies have conversion options that allow a policy owner to exchange part or all of their term policy into a permanent policy that will last forever. These options vary from company to company so its always good to ask an agent or call the insurance company."
    },
    {
        "q": "What Happens When Your Term Life Insurance Runs Out?",
        "a": "\"What happens when your Term life Insurance policy \"\"runs out\"\" or expires or lapses is all the same: Nothing. You no longer have any insurance coverage. And since Term insurance has no cash value you don't get any kind of refund or surrender value. The only exception is if you had purchased a \"\"Return of Premium\"\" rider with your policy. I that case you most likely will receive a portion of the premiums paid in returned to you."
    },
    {
        "q": "When Is Whole Life Insurance Paid Up?",
        "a": "\"Whole Life insurance is called whole life because you never \"\"pay up\"\" and the premium is due each month as long as you live. The exception to that rule is you get the insurance company to use some of the cash value to make the payments for you which is then treated as a policy loan which is then deducted from the death benefits at your death."
    },
    {
        "q": "What Happens When Life Insurance Policy Lapses?",
        "a": "\"Really nothing happens when a life insurance policy lapses. That is to say the policy ends and there is no more insurance. There are a couple things that should happen = you should be notified that the policy is going to lapse and it should be explained how you can prevent that from happening. If the premiums are not paid up to keep the policy in force and it does lapse you should be notified of the provision to reinstate the policy and what steps to take and the time limit within which they must be taken."
    },
    {
        "q": "What Happens When You Cancel Life Insurance?",
        "a": "\"What happens when you cancel life insurance? You end your coverage on the date you provide. Any cash values or unused premium in your policy will be returned to you. With term insurance any unused premium will be refunded. Cancelation should be done in writing as cancelation often requires a signed document."
    },
    {
        "q": "What Happens When Homeowners Insurance Is Cancelled?",
        "a": "\"You will no longer be provided coverage that is afforded under the contract. You will need to re-apply for coverage. Many times a company will reinstate the policy as long as you sign a \"\"no loss letter\"\" stating that you have had no claims during the time the insurance policy has lapsed."
    },
    {
        "q": "What Is Paid Up Whole Life Insurance?",
        "a": "\"Paid up whole life insurance policies refer to the cash value of the plan has reached a point that the death benefit now has enough value to pay your premiums the rest of your life without any further contributions from you. In other words you have achieved free life insurance for the rest of your life. Congratulations!"
    },
    {
        "q": "What Happens When You Stop Paying Life Insurance?",
        "a": "\"That depends on the policy type. In most cases though the policy will be cancelled. Some policy's like universal life and some whole life policies may allow you to miss a payment without cancellations. If you just missed your payment date by a few days and it is the first time that you have missed a payment. I would contact your agent to see if the policy could be re-instated. Please remember every policy is different. Read your policy completely to know what coverage you have and what exclusions there may be or contact your local agent to have them go over the policy with you."
    },
    {
        "q": "What Happens When Term Life Insurance Is Paid Up?",
        "a": ""
    }
]

@app.get("/")
def get_json_data():
    return JSONResponse(content=json_data)
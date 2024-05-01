# Generated by Django 4.0 on 2024-04-30 21:57

from django.db import migrations

CREATED_USER_EMAILS = [
    'admin@example.com', 'tax.user@example.com', 'kashif.ali@example.com', 'asif.ali@example.com',
    'nawaz.shah@example.com'
]


def create_messages(apps, schema_editor):
    """
    Create messages.

    :param apps:
    :param schema_editor:
    """
    _User = apps.get_model('users', 'User')
    _MessagePrompt = apps.get_model('chats', 'MessagePrompt')

    users = _User.objects.filter(email__in=CREATED_USER_EMAILS)

    message_prompts = []
    for user in users:
        file_data = """
        Copy B--To Be Filed With Employee's FEDERAL Tax This information is being funished to the
        Internal Revenue Service. a. Employee's social security number 544299999 b.
        Employer ID number (EIN) 20-1518972 c. Employer's name, address, and
        ZIP code Daniel A Radatti DDS LLC 1250 NE 3rd St Suite B-105 BEND, OR 97701 Return OMB No. 1545-0008 1.
        Wages, tips, other compensation 2. Federal income tax withheld 24854.46 1581.59 3. Social security wages
        4. Social security tax withheld 25854.46 1602.98 5.
        Medicare wages and tips 6. Medicare tax withheld 25854.46 374.89 d.
        Control number e. Employee's name, address, and ZIP code Jackie Coen 9999 Weeping Willow Dr BEND, OR 97701 7.
        Social security tips 8. Allocated tips 9. Verification Code Copy 2--To Be Filed With Employee's State, City,
        or Local Income Tax Return a. Employee's social security number 544299999
        b. Employer ID number (EIN) 20-1518972 c. Employer's name, address,
        and ZIP code Daniel A Radatti DDS LLC 1250 NE 3rd St Suite B-105 BEND, OR 97701 OMB No. 1545-0008 1.
        Wages, tips, other compensation 2. Federal income tax withheld 24854.46 1581.59 3. Social security wages
        4. Social security tax withheld 25854.46 1602.98 5. Medicare wages and tips
        6. Medicare tax withheld 25854.46 374.89 d. Control number e. Employee's name, address,
        and ZIP code Jackie Coen 9999 Weeping Willow Dr BEND, OR 97701 7. Social security tips
        8. Allocated tips 9. Verification Code 10. Dependent care benefits 13. Statutory employee
        14. Other OR STT WH 24.86 Retirement plan Y Third-party sick pay OR 1230074-3
        15. State | Employer's state ID number 11. Nonqualified plans 16. State wages, tips, etc.
        12a. Code See inst. for Box 12 D 1000.00 12b. Code 12c. Code 24854.46 1456.51 17.State income tax
        18. Local wages, tips, etc. 19. Local income tax
        20. Locailty name Form W-2 Wage and Tax Statement FaPY Chor EMPLOYEE S HECORDSISes NgliCe 10, EMpIO)
        ‘Thig tHormation is being furnished to the intemal return,
        a negligence penalty or other sanction may be imposed on you i his income fall to report it
        a. Employee's social security number 544299999 b. Employer ID number (EIN) 20-1518972
        c. Employer's name, address, and ZIP code Daniel A Radatti DDS LLC 1250 NE 3rd St Suite B-105 BEND,
        OR 97701 IRB uo Rares i you ars foie toh a tax is taxable and you OMB No. 1545-0008 1. Wages, tips,
        other compensation 2. Federal income tax withheld 24854.46 1581.59 3. Social security wages
        4. Social security tax withheld 25854.46 1602.98 5. Medicare wages and tips 25854.46
        6. Medicare tax withheld 374.89 d. Control number e. Employee's name, address,
        and ZIP code Jackie Coen 9999 Weeping Willow Dr BEND, OR 97701 7. Social security tips
        8. Allocated tips 9. Verification Code 10. Dependent care benefits} 11. Nonqualified plans
        12a. Code See inst. for Box 12 D 1000.00 13. Statutory employee 14, Other OR STT WH
        24.86 Retirement plan Y Third-party sick pay OR 1230074-3 Employer's state ID number 16.
        State wages, tips, 12b. Code 10. Dependent care benefits 13. Statutory employee 14.
        Other OR STT WH 24.86 Retirement plan Y Third-party sick pay 11. Nonqualified plans OR 1230074-3 15.
        State | Employer's state ID number 16. State wages, tips, etc. 12a. Code See inst. for Box 12 D 1000.00 12b.
        Code 12c. Code 24854.46 1456.51 17.State income tax 18. Local wages, tips, etc. 19. Local income tax
        20. Locailty name DO2QL Deparment of he Treasury ~ internal Revenue Senfee Form W-2 Wage and Tax Statement
        0 Copy 2--To Be Filed With Employee's State, City, or Local Income Tax Return a.
        Employee's social security number 544299999 b. Employer ID number (EIN) 20-1518972 c. Employer's name, address,
        and ZIP code Daniel A Radatti DDS LLC 1250 NE 3rd St Suite B-105 BEND, OR 97701 5. Medicare wages and tips
        25854.46 Department of the Treasury ~ Internal Revenue Service OMB No. 1545-0008 1. Wages, tips,
        other compensation 2. Federal income tax withheld 24854.46 1581.59 3. Social security wages
        4. Social sececutity tax withheld 25854.46 1602.98 6. Medicare tax withheld 374.89 d. Control number e.
        Employee's name, address, and ZIP code Jackie Coen 9999 Weeping Willow Dr BEND, OR 97701 7.
        Social security tips 8. Allocated tips 9. Verification Code 10. Dependent care benefits
        11. Nonqualified plans 13. Statutory employee 14, Other OR STT WH 24.86 Retirement plan Y 24854.46 1456.51
        17.State income tax Third-party sick pay OR 1230074-3 Employer's state ID number 16. State wages, tips,
        12a. Code See inst. for Box 12 D 1000.00 12b. Code 12c. Code 24854.46 1456.51 17.State income tax
        18. Local wages, tips, etc. 19. Local income tax 20. Locailty name 18. Local wages, tips, etc.
        19. Local income tax 20. Locailty name Form W-2 Wage and Tax Statement 2022 Department of the Treasury ~
        Internal Revenue Service Form W-2 Wage and Tax Statement 2022 Department of the Treasury ~
        Internal Revenue Service
        """

        file_data_summary = """This is a W-2 form, which is a tax form used to report an employee's income and taxes withheld to the Internal Revenue Service (IRS). Here's a breakdown of the different sections and fields on the form:

        **Copy B--To Be Filed With Employee's FEDERAL Tax**

        * a. Employee's social security number: XXXXXXXXXX
        * b. Employer ID number (EIN): 20-1518972
        * c. Employer's name, address, and ZIP code: Daniel A Radatti DDS LLC, 1250 NE 3rd St Suite B-105, BEND, OR 97701
        * 1. Wages, tips, other compensation: $24,854.46
        * 2. Federal income tax withheld: $1,581.59
        * 3. Social security wages: $25,854.46
        * 4. Social security tax withheld: $1,602.98
        * 5. Medicare wages and tips: $25,854.46
        * 6. Medicare tax withheld: $374.89
        * d. Control number
        * e. Employee's name, address, and ZIP code: Jackie Coen, 9999 Weeping Willow Dr, BEND, OR 97701

        The other sections of the form, including Copies A, C, and 2, contain the same information, but are filed with different entities (e.g., the IRS, the employee, and the state or local government, respectively).

        **Other sections of the form:**

        * 7. Social security tips
        * 8. Allocated tips
        * 9. Verification Code
        * 10. Dependent care benefits
        * 11. Nonqualified plans
        * 12. Code (with subcodes a, b, and c)
        * 13. Statutory employee
        * 14. Other (OR STT WH 24.86, Retirement plan Y, Third-party sick pay, OR 1230074-3)
        * 15. State (Employer's state ID number)
        * 16. State wages, tips, etc.
        * 17. State income tax
        * 18. Local wages, tips, etc.
        * 19. Local income tax
        * 20. Locality name
        """
        message_prompts.append(_MessagePrompt(
            user=user, role=1, message=file_data))
        message_prompts.append(_MessagePrompt(
            user=user, role=2, message=file_data_summary))
        message_prompts.append(_MessagePrompt(
            user=user, role=1, message='What is the taxable total?'))
        message_prompts.append(_MessagePrompt(
            user=user, role=2, message="""Based on the W-2 form, the taxable total is:
            * Wages, tips, other compensation: $24,854.46 (Box 1)
            * Social security wages: $25,854.46 (Box 3)
            * Medicare wages and tips: $25,854.46 (Box 5)

            Note that these figures include all forms of compensation,
            including tips and other forms of income. 
            The taxable total may be different from the gross pay, 
            as it may not include certain types of income that are not subject to taxation.
            """
        ))

    _MessagePrompt.objects.bulk_create(message_prompts)


def delete_messages(apps, schema_editor):
    """
    Create messages.

    :param apps:
    :param schema_editor:
    """
    _User = apps.get_model('users', 'User')
    _MessagePrompt = apps.get_model('chats', 'MessagePrompt')

    user_ids = _User.objects.filter(
        email__in=CREATED_USER_EMAILS).values_list('id', flat=True)

    _MessagePrompt.objects.filter(user_id__in=user_ids).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0005_messageprompt_role'),
        ('users', '0002_auto_20240430_2149'),
    ]

    operations = [
        migrations.RunPython(create_messages, delete_messages)
    ]
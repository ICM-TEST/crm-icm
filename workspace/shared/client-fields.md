# Client profile fields

Every client has one profile, shaped by [../templates/client-profile.md](../templates/client-profile.md). Fields and fixed lists are structure: adding, removing or changing one is Error 500.

## Personal and contact

| Field | Rule |
|---|---|
| Name | Required |
| Marital status | One of the fixed list below |
| Contact number | Primary |
| Additional contact numbers | Zero or more |
| Email | Primary |
| Additional emails | Zero or more |
| Postal address | |
| Physical address | |
| Income tax number | **Sensitive** |
| ID number | **Sensitive.** Placeholder always present, blank if none |
| Passport number | **Sensitive.** Used when there is no ID number. Placeholder always present |
| Language | English or Afrikaans |
| Bank details | **Sensitive.** Bank, account holder, account number, branch code, account type |

Sensitive fields are never repeated in chat beyond what the person asked to see, never put in a log line's description (write "Bank details changed", not the numbers), and never copied into a note.

## Notes section

Free text on the profile, for things like the client's job title. Not the same as page notes ([work-pages.md](work-pages.md)).

## Classification

| Field | Values |
|---|---|
| Client type | Exactly one, from the fixed list below |
| Rental income | Yes / No |
| Sign-up | Existing / New |
| Status | Active / Inactive |
| Assigned tax practitioner | `Practitioner 1` or `Practitioner 2`, stored with the name as [work-pages.md](work-pages.md) says |
| Office | `Office 1` or `Office 2`, stored the same way |

A new client's Status is Active. Sign-up is asked, never assumed. Balance due starts blank.

Inactive clients keep their folder and history.

## Tax categories

| Category | Rule |
|---|---|
| Income tax | Always Yes. Not editable |
| Provisional tax | Yes / No. Asked when the client is created, no default |

## Balance due

A placeholder field. The system does not update it yet. Leave it blank unless a person gives a figure; do not calculate one.

<!-- TODO (owner): how Balance due gets updated is out of scope for now. -->

## Fixed lists (in the repo)

| List | Values |
|---|---|
| Marital status | Single, Married in community of property, Married out of community of property, Divorced, Widowed |
| Language | English, Afrikaans |
| Rental income | Yes, No |
| Provisional tax | Yes, No |
| Sign-up | Existing, New |
| Status | Active, Inactive |
| Bank account type | As the bank states it; free text |
| Client type | Crew Yachty, General Expat, Non-Res, Local IRP5, Foreign Codes, 6 Quat, Local Other, Inbetal, Unemployed, Protea, Sheltam, Crew, Other, RSA, Non-Resident Letter, Pilots |
| Assigned tax practitioner | Practitioner 1, Practitioner 2 |
| Office | Office 1, Office 2 |

## Options are fixed

Every option on this page is structure. A person selects one and may change which is selected; adding, renaming or removing an option is Error 500. Slot names (practitioners, offices) come from `lists/names.md` in the data folder, read-only: see [work-pages.md](work-pages.md).

## The client log

One file per staff member beside the profile, `<Client Name> – Log – <user name>.md` ([../templates/client-log.md](../templates/client-log.md)): each person's Claude writes only its own, created on their first change. The log is all of them read together, oldest first; a `<Client Name> – Log.md` without a name (from the data load) is part of it, written only to merge a copy of it. Every profile change adds one line: date and time, user name, Google account, description. Append only: never edit or delete a line. A reversed change (Yes, No, Yes) is just more lines.

Descriptions use the names people see, not slots: "Office changed from North to Central", "Practitioner changed from <Name> to <Name>". Sensitive fields stay as "<field> changed", with no values.

User name is the name in the Project instruction. Google account is read from the synced Drive folder's path on this Mac, which contains the signed-in account, for example `.../GoogleDrive-<account>/...`. If the account can't be read from the path, write "account not available".


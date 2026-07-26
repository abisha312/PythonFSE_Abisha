# QA Concepts & Selenium Basics – Hands-On 1
**Digital Nurture 5.0 | Module: QA Concepts & Selenium Basics**

---

# Task 1: Map Testing Types to a Real System

## 1. Testing Types with Real Examples

### Unit Testing

**Description:**  
Unit testing verifies a single function or method independently without interacting with external components like databases.

**Example Test Case:**

Test the function that validates course details before saving.

- **Scenario:** Check whether the `validate_course()` function accepts a valid course name and duration.
- **Input:** Course Name = "Python Programming", Duration = 40
- **Expected Result:** Validation succeeds and returns `True`.

**Testing Type:** Functional Testing

---

### Integration Testing

**Description:**  
Integration testing checks whether multiple components work together correctly.

**Example Test Case:**

Test the `POST /api/courses/` endpoint together with the database.

- Send a valid POST request.
- Verify that the API inserts the course into the database.
- Confirm that the database record matches the submitted data.

**Testing Type:** Functional Testing

---

### System Testing

**Description:**  
System testing validates the complete application as an integrated system.

**Example Test Case:**

1. Send a POST request to create a course.
2. Retrieve all courses using GET.
3. Verify the newly created course appears in the list.
4. Update the course.
5. Delete the course.
6. Verify it no longer exists.

**Expected Result:**  
The complete course management workflow works correctly without errors.

**Testing Type:** Functional Testing

---

### User Acceptance Testing (UAT)

**Description:**  
User Acceptance Testing verifies that the application satisfies business requirements from the end user's perspective.

**Example Test Case:**

A college administrator performs the following tasks:

- Adds a new course.
- Views the course list.
- Updates course information.
- Deletes an outdated course.

**Expected Result:**  
The administrator is able to complete all tasks easily without technical issues.

**Testing Type:** Functional Testing

---

## 2. Functional vs Non-Functional Testing

### Functional Testing

Functional testing verifies whether the application behaves according to the specified requirements.

**Examples:**

- Creating a course
- Updating a course
- Deleting a course
- Viewing course details

---

### Non-Functional Testing Example

#### Performance Testing

**Scenario:**  
Measure how quickly the Course Management API responds when 500 users send requests simultaneously.

**Expected Result:**

- Response time remains below 2 seconds.
- No server crashes.
- API continues serving requests reliably.

This test evaluates **how well** the system performs rather than **what** it does.

---

## 3. Black-Box Testing vs White-Box Testing

| Black-Box Testing | White-Box Testing |
|-------------------|------------------|
| Tester does not know the internal code. | Tester has knowledge of the source code. |
| Focuses on inputs and outputs. | Focuses on code structure, logic, branches, and conditions. |
| Checks whether the software meets user requirements. | Checks whether the implementation is correct internally. |
| Mostly performed by QA Testers. | Mostly performed by Developers. |

### Explanation

In **Black-Box Testing**, the tester only interacts with the application through its interface or API without looking at the code.

**Example:**  
A QA tester sends a POST request and verifies that the course is created successfully.

In **White-Box Testing**, the tester understands the program logic and writes tests to verify loops, conditions, functions, and execution paths.

**Example:**  
A developer tests every branch inside the course validation function.

---

## 4. Formal Test Cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|--------------|------------|----------------|--------------|-----------|
| TC_001 | Create a course with valid details | API server is running | 1. Open API client.<br>2. Send POST request with valid course name and duration.<br>3. Submit request. | HTTP 201 Created. Course is stored in the database successfully. | | |
| TC_002 | Create a course with missing course name | API server is running | 1. Send POST request without course name.<br>2. Submit request. | HTTP 400 Bad Request with validation error message. | | |
| TC_003 | Create a duplicate course | A course with the same name already exists | 1. Send POST request using an existing course name.<br>2. Submit request. | Appropriate error message (409 Conflict or validation error). Duplicate course is not created. | | |

---

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

The typical defect lifecycle followed in software testing is shown below.

```text
New
 ↓
Assigned
 ↓
Open
 ↓
Fixed
 ↓
Retest
 ↓
Verified
 ↓
Closed
```

### Explanation of Each Stage

#### New

- The tester identifies a defect and logs it into the defect tracking system.

#### Assigned

- The defect is assigned to the appropriate developer.

#### Open

- The developer analyzes the issue and starts working on it.

#### Fixed

- The developer resolves the defect and marks it as fixed.

#### Retest

- The QA tester tests the application again using the same test case.

#### Verified

- If the defect no longer exists, QA verifies the fix.

#### Closed

- The defect is officially closed after successful verification.

---

### Alternate Paths

#### Rejected

A defect may be rejected when:

- It is not actually a bug.
- It cannot be reproduced.
- The reported behavior is intended by design.
- There is insufficient information.

---

#### Deferred

A defect is deferred when:

- It is known but will be fixed in a future release.
- Higher priority issues are being addressed first.
- The current release deadline does not allow enough time.

---

## 6. Severity and Priority Classification

### (a) POST /api/courses/ returns 500 Internal Server Error for all requests

**Severity:** Critical

**Priority:** P1 (Highest)

**Justification:**  
The API is completely unusable because users cannot create any courses. This directly impacts the core functionality of the application and requires an immediate fix.

---

### (b) Course names longer than 150 characters are silently truncated

**Severity:** Medium

**Priority:** P2

**Justification:**  
The application continues to function, but user data is modified without warning. This may lead to incorrect records and confusion, so it should be fixed soon.

---

### (c) Swagger documentation contains a typo

**Severity:** Low

**Priority:** P4

**Justification:**  
The typo does not affect the application's functionality. It only impacts documentation quality and can be corrected during a later update.

---

### (d) Login occasionally returns 401 despite correct credentials

**Severity:** High

**Priority:** P1

**Justification:**  
Although the issue is intermittent, users may be unable to log in even with valid credentials. Since login is essential and the problem is unpredictable, it deserves immediate attention.

---

## 7. Defect Report

### Defect Report

**Defect ID:** DEF-001

**Title:**  
POST /api/courses/ returns HTTP 500 Internal Server Error for every request.

**Environment:**

- Windows 11
- Python 3.x
- FastAPI
- SQL Server
- Swagger UI

**Build Version:**  
Version 1.0

**Severity:**  
Critical

**Priority:**  
P1

### Steps to Reproduce

1. Start the Course Management API.
2. Open Swagger UI.
3. Navigate to `POST /api/courses/`.
4. Enter valid course details.
5. Click **Execute**.

### Expected Result

The API should create the course successfully and return **HTTP 201 Created**.

### Actual Result

The API returns **HTTP 500 Internal Server Error** and no course is saved to the database.

### Attachments

- Screenshot of 500 Internal Server Error.

---

## 8. Difference Between Severity and Priority

| Severity | Priority |
|----------|----------|
| Measures how much the defect affects the system. | Measures how urgently the defect should be fixed. |
| Determined mainly by QA based on impact. | Determined by QA, developers, or project managers based on business needs. |

### Real-World Example

Imagine an e-commerce website where the **"Terms and Conditions"** page crashes when opened.

- **Severity:** High, because the page itself is broken.
- **Priority:** Low, because most customers can still browse products, place orders, and make payments without accessing that page.

On the other hand, suppose the company's CEO is giving a live product demonstration tomorrow, and the homepage displays the company name with a spelling mistake.

- **Severity:** Low, because the typo does not affect functionality.
- **Priority:** High, because it impacts the company's professional image during an important event and should be corrected immediately.

This example shows that **severity indicates the technical impact of a defect, while priority determines how quickly it should be resolved based on business requirements.**

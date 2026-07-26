# SDLC vs TDLC – V-Model & Agile QA Integration
**Module:** QA Concepts & Selenium Basics  
**File:** `v_model_analysis.md`
---

# TASK 1: V-MODEL MAPPING

## 9. Complete V-Model Diagram

The V-Model illustrates how each phase of the Software Development Life Cycle (SDLC) corresponds to a specific phase in the Testing Life Cycle (TDLC). Testing activities are planned alongside development activities, ensuring quality is built into the software from the beginning rather than being checked only after coding is complete.

```text

      DEVELOPMENT (SDLC)                     TESTING (TDLC)

      Requirements Analysis               Acceptance Testing
               \                                 /
                \                               /
                 \                             /
                  \                           /
              System Design             System Testing
                    \                       /
                     \                     /
                      \                   /
              Architecture Design    Integration Testing
                         \              /
                          \            /
                           \          /
                   Module Design    Unit Testing
                              \     /
                               \   /
                                \ /
                              CODING
```
```

The left side of the V-Model represents the development phases, while the right side represents the corresponding testing phases. Coding forms the bottom vertex, connecting development and testing.

---

## 10. SDLC and TDLC Phase Mapping & Test Artifacts

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced During Development Phase |
| :--- | :--- | :--- |
| **Requirements Analysis** | Acceptance Testing | Acceptance Test Plan, User Acceptance Test Scenarios, Requirement Traceability Matrix (RTM) |
| **System Design** | System Testing | System Test Plan, End-to-End System Test Cases |
| **Architecture Design** | Integration Testing | Integration Test Plan, Interface Test Cases, API Contract Test Cases |
| **Module Design** | Unit Testing | Unit Test Cases, Unit Test Suite, Stubs & Drivers |
| **Coding** | Unit Test Execution | Executable Source Code and Unit Test Execution Results |

### Explanation

#### Requirements Analysis ↔ Acceptance Testing

During the requirements phase, QA reviews business requirements and prepares acceptance test plans and acceptance criteria. The Requirement Traceability Matrix (RTM) is also created to ensure every requirement is covered by at least one test case.

#### System Design ↔ System Testing

When the overall system design is completed, QA prepares system test plans and end-to-end test cases to validate the complete application from the user's perspective.

#### Architecture Design ↔ Integration Testing

Architecture design defines how different modules communicate. QA prepares integration test plans, interface test cases, and API contract tests to verify interactions between components.

#### Module Design ↔ Unit Testing

Developers design individual modules and functions. Unit test cases, unit test suites, and supporting stubs or drivers are prepared to verify each module independently.

#### Coding ↔ Unit Test Execution

Developers implement the application and execute unit tests before integrating the modules into the complete system.

---

## 11. Entry and Exit Criteria for Testing Levels

### 1. Unit Testing

**Entry Criteria**

- Module design document is finalized and approved.
- Source code has been written without compilation errors.
- Unit test cases/scripts are prepared and reviewed.
- Development environment is ready.

**Exit Criteria**

- All planned unit test cases have been executed successfully.
- Code coverage meets the project's minimum threshold (for example, 80%).
- All critical unit-level defects are resolved and verified.
- Unit testing report is completed.

---

### 2. Integration Testing

**Entry Criteria**

- Unit testing is completed and signed off.
- Individual modules are integrated.
- Integration test cases are prepared.
- Integration testing environment and test data are available.

**Exit Criteria**

- All interface and API integration test cases have been executed.
- Data flow between integrated modules works correctly.
- No unresolved Critical or High severity integration defects remain.
- Integration testing summary report is completed.

---

### 3. System Testing

**Entry Criteria**

- Integration testing is successfully completed.
- Complete application build is deployed to the QA environment.
- System test plan and end-to-end test cases are approved.

**Exit Criteria**

- All planned system test cases have been executed.
- No open Critical or High severity defects remain.
- Application satisfies all functional requirements.
- System testing summary report is approved.

---

### 4. Acceptance Testing (UAT)

**Entry Criteria**

- System testing has been completed successfully.
- UAT environment is configured with production-like data.
- User stories and acceptance criteria are available.
- Business users are ready to perform validation.

**Exit Criteria**

- All business scenarios have been executed successfully.
- Formal business sign-off is received from stakeholders.
- All acceptance criteria are satisfied.
- No blocking business issues remain.
- Application is approved for production deployment.

---

## 12. Early QA Engagement Points in the Course Management API

### 1. Requirements Review Phase

**QA Engagement**

QA participates in requirement review meetings before development begins to identify ambiguous, incomplete, or conflicting requirements.

**Course Management API Example**

Before development starts, QA reviews the requirements for the `POST /api/courses/` endpoint to ensure validation rules are clearly defined, such as mandatory fields, maximum course name length, unique course codes, and valid credit ranges.

---

### 2. Architecture & API Design Phase

**QA Engagement**

QA reviews API specifications, Swagger documentation, database schema, and overall application design before coding begins.

**Course Management API Example**

QA verifies endpoint URLs, request and response formats, HTTP status codes (`201 Created`, `400 Bad Request`, `404 Not Found`, `409 Conflict`), and database relationships to ensure they meet the business requirements before implementation.

---

# TASK 2: AGILE QA AND SHIFT-LEFT TESTING

## 13. Problems with Waterfall Testing in the Course Management API

### 1. Defects Are Discovered Too Late

Since testing begins only after development is completed, requirement misunderstandings may remain unnoticed until the testing phase, making them more expensive to fix.

### 2. Bug Fixing Becomes More Expensive

A defect discovered late may require modifications to API logic, database schema, frontend integration, and documentation, increasing both development effort and project cost.

### 3. Delayed Project Delivery

If serious defects are identified near the end of development, additional debugging and retesting can delay the project release and reduce the overall testing time available.

---

## 14. QA Responsibilities in Agile Ceremonies

### Sprint Planning

QA reviews user stories, identifies test scenarios, discusses acceptance criteria, highlights testing effort and potential risks, and contributes to sprint estimation discussions.

---

### Daily Standup

QA shares testing progress, reports newly discovered defects, discusses blockers (such as unavailable test environments or failed API deployments), and collaborates with developers to resolve issues quickly.

---

### Sprint Review

QA validates that completed features satisfy the agreed acceptance criteria before they are demonstrated to stakeholders and confirms that completed functionality is ready for acceptance.

---

### Sprint Retrospective

QA discusses lessons learned, identifies process improvements, recommends better testing practices, suggests automation opportunities, and helps improve quality in future sprints.

---

## 15. Shift-Left Testing Practices Applied to the Course Management API

### (a) Reviewing Requirements for Testability

QA reviews requirements before development begins to ensure they are complete, measurable, and testable.

**Application**

Review the `POST /api/courses/` user story to confirm that validation rules (such as mandatory fields, course code format, and credit limits) are clearly specified.

---

### (b) Writing Test Cases Before Code (TDD/BDD)

QA prepares test cases before implementation so developers understand the expected system behavior.

**Application**

Write automated test scenarios for successful course creation, invalid requests, and duplicate course codes before the API endpoint is implemented.

---

### (c) Static Code Analysis

Developers use static analysis tools to identify coding issues without executing the application.

**Application**

Use tools such as **Flake8**, **Pylint**, or **SonarQube** within the CI/CD pipeline to detect coding standard violations, security vulnerabilities, and potential bugs in the FastAPI project.

---

### (d) API Contract Testing Before Integration

QA validates API contracts before frontend integration begins.

**Application**

Use **Postman** or **Pact** to verify that the `POST /api/courses/` endpoint follows the Swagger/OpenAPI specification, including request payloads, response schemas, and HTTP status codes.

---

## 16. Acceptance Criteria (Given–When–Then)

```
Feature: Create New Course

As a college administrator,
I want to create a new course,
So that students can enroll in it.

Scenario: Successfully create a new course
Given the college administrator is logged into the Course Management System
When the administrator creates a new course with valid details
Then the course should be created successfully
And the system should display a confirmation message
And the course should be stored in the database

Scenario: Prevent duplicate course creation
Given a course with the same course code already exists
When the administrator creates another course using the same course code
Then the system should prevent the course from being created
And an error message stating "Course code already exists" should be displayed

Scenario: Missing mandatory fields
Given the administrator is creating a new course
When one or more required fields are left empty
Then the system should display validation messages for the missing fields
And the course should not be created
```

---

# Conclusion

This hands-on demonstrated how the Software Development Life Cycle (SDLC) and the Testing Life Cycle (TDLC) are connected through the V-Model. It explained the relationship between development and testing phases, the test artifacts produced during each stage, and the entry and exit criteria for every testing level. It also highlighted the importance of involving QA early in the development process, described the responsibilities of QA engineers throughout Agile ceremonies, explored practical Shift-Left testing techniques, and illustrated how business requirements can be converted into executable acceptance criteria using the Given–When–Then format. These practices help teams detect defects earlier, improve software quality, reduce development costs, and deliver reliable applications more efficiently.

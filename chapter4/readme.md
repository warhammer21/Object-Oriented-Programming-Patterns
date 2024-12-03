# Role-Based Authentication and Authorization System

## **Overview**
This project implements a **Role-Based Authentication and Authorization System** designed for a food delivery platform. It includes multiple user roles (Admin, Customer, and Delivery Personnel) with distinct permissions and actions. The system ensures that only authorized users can perform specific tasks by combining authentication and authorization patterns.

---

## **Key Features**
1. **Authentication**:
   - Users can log in with their username and password.
   - Passwords are encrypted using the SHA-256 hashing algorithm.

2. **Authorization**:
   - Role-based permissions control access to specific functionalities.
   - Only users with the required permissions can perform certain actions.

3. **User Roles**:
   - **Customer**: Can browse menus and place orders.
   - **Delivery Personnel**: Can accept delivery assignments.
   - **Admin**: Can manage menus and orders.

4. **Extensibility**:
   - The design allows adding new roles or permissions with minimal changes.

---

## **Project Structure**
### Classes
1. **User**:
   - Base class for all users.
   - Handles password encryption and validation.

2. **Customer, DeliveryPersonnel, Admin**:
   - Derived classes representing specific user roles.
   - Each role can perform actions unique to their responsibilities.

3. **Authenticator**:
   - Manages user registration and login.
   - Tracks login states for all users.

4. **Authorizor**:
   - Manages role-based permissions.
   - Verifies if a user is authorized to perform a specific action.

5. **Custom Exceptions**:
   - Handles errors like invalid credentials, insufficient permissions, and more.

---

## **Design Pattern**
This project uses a combination of:
1. **Object-Oriented Design**:
   - Encapsulation of user roles and their actions.
   - Reusability of the `User` class as a base for all roles.

2. **Authentication and Authorization**:
   - Clear separation of concerns:
     - **Authentication** ensures users are who they claim to be.
     - **Authorization** ensures users have the right to perform certain actions.

3. **Role-Based Access Control (RBAC)**:
   - Role-specific permissions enforce security and access control.

4. **Single Responsibility Principle**:
   - Each class has a single, well-defined responsibility (e.g., `Authenticator` for login management, `Authorizor` for permissions).

---

## **Learnings**
### Key Takeaways from this Design:
1. **Separation of Concerns**:
   - Authentication and authorization are handled independently, making the system modular and maintainable.

2. **Role-Based Access Control**:
   - Assigning permissions to roles simplifies user management and enhances security.

3. **Error Handling**:
   - Custom exceptions improve debuggability and ensure robust input validation.

4. **Extensibility**:
   - Adding new roles or actions requires minimal changes, adhering to open/closed principles.

5. **Security**:
   - Storing encrypted passwords ensures data security, reducing vulnerabilities in authentication.

---



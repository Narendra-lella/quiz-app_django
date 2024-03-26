Access the application in your web browser at the specified address.

## Roles
- Admin or manager can add the questions.
- Teacher or Head of the Department can access all the questions listed and can modify.
- Students can get the question to take the test.

## End Points
- ../auth/register/ -- POST
- ../auth/login -- POST
  Here you will get the access token and refresh token for authentication.
- ../api/auth/questions/ -- GET
  Get list of all questions.
- ../api/auth/questions/{question_id} -- GET
  Get particular question.
- ../api/auth/question/{question_id} -- PUT
  Update the questions.
- ../api/auth/delete/question -- DELETE

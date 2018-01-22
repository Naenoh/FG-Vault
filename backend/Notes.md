##### regexp search example
`Post.query.filter(text("title ~* :regexp")).params(regexp='(?=.*sol)(?=.*bnb)').all()`
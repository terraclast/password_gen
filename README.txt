Here is a simple password program designed to be used in the CLI.  It is python based.

It can create any specified length of password with four levels of complexity:
1.) Weak        --  Only uses lowercase letters.
2.) Middling    --  Uses both uppercase and lowercase letters.
4.) Strong      --  Uses lowercase and uppercase letters, and numbers.
5.) Beast       --  Uses lowercase, uppercase, numbers, and punctuation symbols.

It currently only uses the random library, but I would eventually like to add an entropy parameter for more fine-grained control over the password strength.

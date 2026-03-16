# ntgen = Non-Terminal Generator

Small(ish) Python script that generates a header in the c programming
language that contains IDs for all of the defined non-terminal, based
on the production rules of a passed
[Bison](https://www.gnu.org/software/bison/manual/) file.

Example command:

```sh
python3 src/main.py bison.y
```

Here's an example output:

```c
#ifndef INCLUDE_NTGEN_NTERM_H_
#define INCLUDE_NTGEN_NTERM_H_
#define PROGRAM 1
#define DECLR_LIST 2
#define FUNC_DECLR 3
#define VAR_DECLR 4
#define DECLR 5
#define RET_TYPE 6
#define INIT_PREFIX 7
#define INTIALIZER_LIST 8
#define ARRAY_INTIALIZER 9
#define INTIALIZER 10
#define ID_DECLR_LIST 11
#define ID_DECLR 12
#define VAR_DECLR_LIST 13
#define PARAM_LIST 14
#define PARAM 15
#define BLOCK 16
#define STMT_LIST 17
#define STMT 18
#endif  // INCLUDE_NTGEN_NTERM_H_
```

You can change the start ID by passing an argument (see usage).
Default is to start at one and increment IDs from there.

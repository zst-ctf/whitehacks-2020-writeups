#include <gmp.h>

// https://wiremask.eu/articles/fermats-prime-numbers-factorization/
// gcc fermet_factorise.c -lgmp

void fermat_factor(mpz_t p, mpz_t q, mpz_t N);

int main()
{
    mpz_t N;
    mpz_t p, q;

    mpz_init(N);
    mpz_init(p);
    mpz_init(q);

    mpz_set_str(N, "1256656480120450597072003081650664247724680264297536167141726306997142058813860712447498826449451514352875011768202001668178501530482872870615464922095824146502601180079982667001473444407850861123511536903340611829437862912575888515400255728038035391942435700006309694619049809051715181593028933225306263279801681907232318764723173740565723029660057614708655761208626229572919039715738878236340790655662803118743086409128997507998047948092769887723393691045315067", 10);
    fermat_factor(p, q, N);

    gmp_printf("p = %Zd\n", p);
    gmp_printf("q = %Zd\n", q);

    mpz_clear(p);
    mpz_clear(q);
    mpz_clear(N);

    return 0;
}

void fermat_factor(mpz_t p, mpz_t q, mpz_t N)
{
    mpz_t a, b;

    mpz_init(a);
    mpz_init(b);

    mpz_sub_ui(a, N, 1);
    mpz_sqrt(a, a);
    mpz_add_ui(a, a, 1);

    while (1)
    {
        mpz_mul(b, a, a);
        mpz_sub(b, b, N);

        if (mpz_perfect_square_p(b))
            break;

        mpz_add_ui(a, a, 1);
    }

    mpz_sqrt(p, b);
    mpz_sqrt(q, b);
    mpz_add(p, a, p);
    mpz_sub(q, a, q);

    mpz_clear(a);
    mpz_clear(b);
}
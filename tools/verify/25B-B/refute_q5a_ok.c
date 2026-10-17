struct a{int x;}; struct b{struct a in;}; struct c{struct a*p;}; struct d{struct b*q; struct a in; struct c cc;}; struct s{struct s*next;int x;};
int main(){struct a A; struct d D; (void)A;(void)D;return 0;}

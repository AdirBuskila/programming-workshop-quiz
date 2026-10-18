double f(){return 1.5;}
int main(){ double (*p)()=f; double (**q)()=&p; return (int)(*q)(); }

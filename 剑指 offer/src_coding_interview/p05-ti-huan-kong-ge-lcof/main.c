// "We are happy."
//  1234567890123
// "We%20are%20happy."
//  12345678901234567
char* replaceSpace(char* s){
	if (s == NULL){
		return s;
	}
	int i,
	    s_len,
	    new_s_len,
	    ind;

	s_len = 0;
	new_s_len = 0;
	for(i = 0; s[i] != '\0' ; i ++){
		if(s[i] == ' '){
			new_s_len += 3;
		}else{
			new_s_len += 1;
		}
        s_len += 1;
	}
    s_len += 1;
    new_s_len += 1;
    // printf("s=%s\n", s);
    // printf("sizeof(s[0])=%d\n", sizeof(s[0]));
    // printf("sizeof(s)=%d\n", sizeof(s));
    // printf("s_len=%d\n", s_len);
    // printf("new_s_len=%d\n", new_s_len);

	char *new_s = (char *)malloc(new_s_len * sizeof(s[0]));
	ind = 0;
	for(i = 0; i < s_len; i ++){
		if (s[i] == ' '){
			new_s[ind] = '%';
			ind ++;
			new_s[ind] = '2';
			ind ++;
			new_s[ind] = '0';
			ind ++;
		}else{
			new_s[ind] = s[i];
            ind ++;
		}
	}

	return new_s;
}


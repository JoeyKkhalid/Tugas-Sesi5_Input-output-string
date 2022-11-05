{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "121d8c20",
   "metadata": {},
   "outputs": [],
   "source": [
    "#tugas PD sesi 5 \n",
    "#Jika terdapat kalimat UNIVERSITAS NUSA PUTRA SUKABUMI buatlah kode\n",
    "#program untuk menampilkan output:\n",
    "#a. putra nusa\n",
    "#b. NIVERSITAS NSA PTRA SKABMI\n",
    "#C. SUKABUMI PUTRA NUSA UNIVERSITAS\n",
    "#d. UNPS\n",
    "#e. TAS SAPU BUMI\n",
    "\n",
    "#deklarasi varibel\n",
    "kalimat = \"UNIVERSITAS NUSA PUTRA SUKABUMI\"\n",
    "\n",
    "#membuat output point a dengan mengambil index dan membuanya menjadi huruf kecil \n",
    "print(\"point a :\",kalimat[17:22].lower(),kalimat[12:16].lower()) #output : putra nusa\n",
    "#membuat output point b \n",
    "print(\"point b :\",kalimat[1:11],kalimat[12]+kalimat[14:16],kalimat[17]+kalimat[19:22],kalimat[23]+kalimat[25:28]+kalimat[29:31]) #output : NIVERSITAS NSA PTRA SKABMI\n",
    "#membuat output point c \n",
    "print(\"point c :\",kalimat[23:31],kalimat[17:22],kalimat[12:16],kalimat[0:11]) #output : SUKABUMI PUTRA NUSA UNIVERSITAS\n",
    "#membuat output point d\n",
    "print(\"point d :\",kalimat[0]+kalimat[12]+kalimat[17]+kalimat[23]) #output : UNPS \n",
    "#membuat output point e\n",
    "print(\"point e :\",kalimat[8:11],kalimat[14:16]+kalimat[17:19],kalimat[27:31]) #output : TAS SAPU BUMI\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

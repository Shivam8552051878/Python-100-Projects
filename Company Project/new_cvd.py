import json
import datetime
master_sales = [
 {
  "sr.no.": 1,
  "Date": "10-Oct-16",
  "Particulars": "Parth Gems",
  "Address": "EC-4020,Bharat Diamond Bourse,, BKC,Mumbai-400004, Mob.",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820510422,
  "NAME": "Paresh N Shah"
 },
 {
  "sr.no.": 2,
  "Date": "11-Oct-16",
  "Particulars": "Sejal Exports (I) Pvt. Ltd.",
  "Address": "301,Navpad Apartment,, Jadakhadi, Mahidharpura, Surat",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9867098700,
  "NAME": "taroon",
  "EMAIL ID": "sejalexport301@hotmail.com"
 },
 {
  "sr.no.": 3,
  "Date": "18-Oct-16",
  "Particulars": "Hardik Gems",
  "Address": "FC-4030 , bdb",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9892188110,
  "NAME": "sanket shah",
  "EMAIL ID": "hardikgems1@gmail.com"
 },
 {
  "sr.no.": 4,
  "Date": "31-Mar-17",
  "Particulars": "Shilpa Subramanya Acharya",
  "Address": "4-Row House, Laxmi Palace ,, Laxmi Park, Kakakia, Meera Road E Thane, Mumbai",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 5,
  "Date": "08-May-17",
  "Particulars": "JAY GEMS",
  "Address": "905,Princess Plaza, Varacha Road, Surat, 395006",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9328105027,
  "NAME": "jerambhai lavjibhai",
  "EMAIL ID": "jay_gemss@yahoo.co.in"
 },
 {
  "sr.no.": 6,
  "Date": "13-May-17",
  "Particulars": "Diamond Source",
  "Address": "CC-3200 bdb",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 7,
  "Date": "01-Jun-17",
  "Particulars": "Keeva Diamond",
  "Address": "Flat No.1003,10th Floor,Satya Ki Nagari, P.B. Marg,, Near Deepak Cinema, Lower Parel Delisle Road, Mumbai - 400013",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 8,
  "Date": "09-Jun-17",
  "Particulars": "Mira Gems",
  "Address": "DC-8210,\"D' Tower,, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (E), Mumbai",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9072,
  "NAME": "sanket"
 },
 {
  "sr.no.": 9,
  "Date": "10-Jun-17",
  "Particulars": "Yogeshwar Diamonds",
  "Address": "DC-9030 Bharat Diamond Bourse, Bandra Kurla Complex, Bandra East, Mumbai",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9819883343,
  "NAME": "Amit bhai",
  "EMAIL ID": "mumbai@yageshwar.group"
 },
 {
  "sr.no.": 10,
  "Date": "24-Jul-17",
  "Particulars": "AASHNI GEMS",
  "Address": "AW-4130, BHARAT DIAMOND BOURSE,, BANDRA KURLA COMPLEX, BANDRA (EAST),, MUMBAI",
  "GSTIN\/UIN": "27AAAFA2153Q1ZD",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 11,
  "Date": "08-Aug-17",
  "Particulars": "S.Vinodkumar Diamonds Pvt. Ltd.",
  "Address": "BW-3010,Bharat Diamond Bourse, BKC, Bandra(E), Mumbai",
  "GSTIN\/UIN": "27AAICS5514N1ZW",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9594261201,
  "NAME": "hema madam",
  "EMAIL ID": "vinod.wadhawal@indusind.com"
 },
 {
  "sr.no.": 12,
  "Date": "21-Aug-17",
  "Particulars": "Ashish Impex",
  "Address": "402,Orion Business Park,, Nehru Road,Santacruz(East), Mumbai",
  "GSTIN\/UIN": "27AAFFA6111K1ZM",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820152691,
  "NAME": "hitesh bhai"
 },
 {
  "sr.no.": 13,
  "Date": "31-Aug-17",
  "Particulars": "Rashi Gems",
  "Address": "JE 2200 Bharat Diamond Bourse, Bandra Kurla Complex, Bandra East, Mumbai",
  "GSTIN\/UIN": "27AEEPB1159D1Z2",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 14,
  "Date": "30-Nov-17",
  "Particulars": "Mira Gems (Surat)",
  "Address": "160,Shreeji Chambers,, Opp.Sadhana Society,, Mini Bazar,, Varachha Road,, Surat",
  "GSTIN\/UIN": "24AAXFM9362Q1Z3",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9072,
  "NAME": "sanket"
 },
 {
  "sr.no.": 15,
  "Date": "13-Dec-17",
  "Particulars": "K.Chandrakant & Co International Pvt.Ltd",
  "Address": "AE\/6011 Bharat Diamond Bourse,, BKC,, Bandra (E), Mumbai",
  "GSTIN\/UIN": "27AAECK3555D1ZO",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 16,
  "Date": "04-Jan-18",
  "Particulars": "V. MILAN & CO",
  "Address": "CW- 4091, Bharat Diamond Bourse, BKC,, Bandra(E), Mumbai",
  "GSTIN\/UIN": "27AAJFV1424C1ZG",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9819699993,
  "NAME": "Viken c doshi",
  "EMAIL ID": "v.milan@live.com"
 },
 {
  "sr.no.": 17,
  "Date": "05-Jan-18",
  "Particulars": "Diksha Diamonds",
  "Address": "Romnambr 16 2nd Floor, Maradiya Bhavan 6, Khetvadi",
  "GSTIN\/UIN": "27BJHPS3618F1Z2",
  "QUantity": "1 Unit",
  "EMAIL ID": "m"
 },
 {
  "sr.no.": 18,
  "Date": "18-Jan-18",
  "Particulars": "Leora Jewellery",
  "Address": "55-A Surat Special Economic Zone, Sachin, Surat",
  "GSTIN\/UIN": "24AACFL7071Q1ZV",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 19,
  "Date": "18-Jan-18",
  "Particulars": "Ayan Impex",
  "Address": "B\/5, 1st Floor,GK Chambers, Above Surati Khaman House, Kohinoor Road,Mini Bazar, Varachha",
  "GSTIN\/UIN": "24ABHFA0465B2Z1",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 20,
  "Date": "01-Feb-18",
  "Particulars": "Varia Exports",
  "Address": "1st Floor,101\/b, Bhagyodaya Apartment,, Sarojani Road,, Vile Parle West, Mumbai Suburban",
  "GSTIN\/UIN": "27ABGPV5373A1ZK",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 21,
  "Date": "16-Feb-18",
  "Particulars": "The Lalit Gems Co.",
  "Address": "CC-3031,Bharat Diamond Bourse,, BKC, Bandra(E), Mumbai",
  "GSTIN\/UIN": "27AAGFT5346L1ZP",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 22,
  "Date": "10-Mar-18",
  "Particulars": "Aneri Jewels",
  "Address": "B-14-503, Krishna Apartment,CHS LTD., Shanti Park,Nr.ST.Xaviers School,, Mira Road(East),, Thane",
  "GSTIN\/UIN": "27AUGPP9723M1ZW",
  "QUantity": "2 Unit",
  "CONTACT NO.": 9820436789,
  "NAME": "Amit bhai",
  "EMAIL ID": "anerijewels@gmail.com"
 },
 {
  "sr.no.": 23,
  "Date": "14-Mar-18",
  "Particulars": "Naice Jewels Pvt Ltd",
  "Address": "230,233,236, Pragati Industrial Estate, N.M.Joshi Marg, Lower Parel (E), Mumbai",
  "GSTIN\/UIN": "27AACCN3008N1ZE",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820130472,
  "NAME": "Nimesh",
  "EMAIL ID": "nimishnaice@gmail.com"
 },
 {
  "sr.no.": 24,
  "Date": "02-Apr-18",
  "Particulars": "Rasiklal Mohanlal Gandhi",
  "Address": "30,Burtolla Street, Kolkata",
  "GSTIN\/UIN": "19AALFR1189A1Z5",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9594210742,
  "NAME": "Alpa rashik"
 },
 {
  "sr.no.": 25,
  "Date": "02-Apr-18",
  "Particulars": "LAXMI DIAMOND PRIVATE LIMITED",
  "Address": "EW 2200 BHARAT DIAMOND BOURSE, BANDRA KURLA COMPLEX, BANDRA EAST, MUMBAI - 400051",
  "GSTIN\/UIN": "27AABCL1815G1ZT",
  "QUantity": "1 Unit",
  "CONTACT NO.": 8850300273,
  "NAME": "Shubam"
 },
 {
  "sr.no.": 26,
  "Date": "04-Apr-18",
  "Particulars": "PARAM EXPORTS",
  "Address": "JE 6100-6110, Bharat Diamond Bourse, Bandra Kurla Complex, Bandra(E), Mumbai",
  "GSTIN\/UIN": "27AAAFP2983M1ZS",
  "QUantity": "1 Unit",
  "CONTACT NO.": 239690074,
  "NAME": "dhamji bhai",
  "EMAIL ID": "pradip@paramexport.in"
 },
 {
  "sr.no.": 27,
  "Date": "28-Apr-18",
  "Particulars": "K.Chandrakant & Co International Pvt.Ltd",
  "Address": "AE\/6011 Bharat Diamond Bourse,, BKC,, Bandra (E), Mumbai",
  "GSTIN\/UIN": "27AAECK3555D1ZO",
  "QUantity": "-1 Unit"
 },
 {
  "sr.no.": "28",
  "Date": "03-May-18",
  "Particulars": "GEM STAR",
  "Address": "506,Prasad Chambers, Swadeshi Mill Compound, Opera House, Mumbai",
  "GSTIN\/UIN": "27AAFFG5273L1Z1",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 29,
  "Date": "03-May-18",
  "Particulars": "HARSHID EXPORTS",
  "Address": "HE – 8120, 8TH FLOOR, BHARAT DIAMOND BOURSE, BANDRA KURLA COMPLEX, BANDRA (E), MUMBAI",
  "GSTIN\/UIN": "27AADFH1829H1ZH",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820140188,
  "NAME": "Harshid",
  "EMAIL ID": "harshidexports@gmail.com"
 },
 {
  "sr.no.": 30,
  "Date": "03-May-18",
  "Particulars": "RAMKRISHNA DIAMOND",
  "Address": "5-6 DONGREWADI, OPP AFIL TOWER, BESIDE ROYAL ARCADE L.H.ROAD, VARACHHA, SURAT",
  "GSTIN\/UIN": "24AAKFR3760Q1ZL",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9375209935,
  "NAME": "Ghanshyam bhai",
  "EMAIL ID": "account@ramkrishnadiamond.com "
 },
 {
  "sr.no.": 31,
  "Date": "05-May-18",
  "Particulars": "Vithal Gems Pvt Ltd.",
  "Address": "JE-8150,Bharat Diamond Bourse,, Bandra Kurla Complex, Bandra (E), Mumbai",
  "GSTIN\/UIN": "27AAECV5637M1ZR",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 32,
  "Date": "07-May-18",
  "Particulars": "Kumbh Gems",
  "Address": "FW 3150, BHARAT DIAMOND BOURSE, BANDRA KURLA COMPLEX, BANDRA EAST, MUMBAI",
  "GSTIN\/UIN": "27AADFK5586G1Z2",
  "QUantity": "1 Unit",
  "EMAIL ID": "dhabal@kumbhgems.com"
 },
 {
  "sr.no.": 33,
  "Date": "26-May-18",
  "Particulars": "Bharodia Exports",
  "Address": "1103\/A Soni Tower, Near Ram Nagar, Simpoli Road, Borivali(W), Mumbai",
  "GSTIN\/UIN": "27AAFFB8760R1ZO",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 34,
  "Date": "28-May-18",
  "Particulars": "SHRI HARI GEMS",
  "Address": "CW\/5040-30.Bharat Diamond Bourse, Bandra Kurla Complex,, Bandra(E), Mumbai",
  "GSTIN\/UIN": "27AAKFS8410N1ZN",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820022809,
  "NAME": "Mayur harshad",
  "EMAIL ID": "shrgems@gmail.com"
 },
 {
  "sr.no.": 35,
  "Date": "29-May-18",
  "Particulars": "C. V. IMPEX",
  "Address": "203\/204, SIDDHIDEEP APT,, 7 MAHANT ROAD, VILE PARLE (EAST), MUMBAI",
  "GSTIN\/UIN": "27AAAFC3796K1Z4",
  "QUantity": "1 Unit",
  "CONTACT NO.": 8291528391,
  "NAME": "Harsh bhai"
 },
 {
  "sr.no.": 36,
  "Date": "18-Jun-18",
  "Particulars": "SUPARTH EXPORTS",
  "Address": "CC-3171,Bharat Diamond Bourse,, Bandra Kurla Complex, Bandra(E), Mumbai",
  "GSTIN\/UIN": "27AAKFS8992B1ZP",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9819830319,
  "NAME": "bharat bhai",
  "EMAIL ID": "suparthexport@gmail.com"
 },
 {
  "sr.no.": 37,
  "Date": "10-Jul-18",
  "Particulars": "Spectrum Jewelmart Private Limited",
  "Address": "B-3, Dhruv Marg, Vijay Path, Tilak Nagar, Jaipur",
  "GSTIN\/UIN": "08AAMCS5865J1ZM",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 38,
  "Date": "18-Jul-18",
  "Particulars": "S Jogani Exports Private Limited",
  "Address": "DW - 3010,D TOWER WEST WING, BHARAT DIAMOND BOURSE, BKC BANDRA (E), MUMBAI",
  "GSTIN\/UIN": "27AALCS4862J1ZS",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9920360074,
  "NAME": "Paresh bhai"
 },
 {
  "sr.no.": 39,
  "Date": "18-Jul-18",
  "Particulars": "P.Dilipkumar & Co.",
  "Address": "JE-7050 7th Floor,, Bharat Diamond Bourse,, G Block, Bandra East, Mumbai",
  "GSTIN\/UIN": "27AACFP3009N1Z5",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 40,
  "Date": "18-Aug-18",
  "Particulars": "S Jogani Exports Private Limited",
  "Address": "DW - 3010,D TOWER WEST WING, BHARAT DIAMOND BOURSE, BKC BANDRA (E), MUMBAI",
  "GSTIN\/UIN": "27AALCS4862J1ZS",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9920360074,
  "NAME": "Paresh bhai"
 },
 {
  "sr.no.": 41,
  "Date": "20-Aug-18",
  "Particulars": "Jaydeep Gems",
  "Address": "6th Floor,487 Murad Mansion, S.V.P. Road, Opera House, Mumbai",
  "GSTIN\/UIN": "27AAEPJ2168C1Z1",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 42,
  "Date": "24-Aug-18",
  "Particulars": "P Maitri and Co",
  "Address": "GW-2060,2nd Floor,Bharat Diamond Bourse,, Bandra Kurla Complex, Bandra East, Mumbai",
  "GSTIN\/UIN": "27AAEFP2470M1ZY",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9819259025,
  "NAME": "mahesh bhai"
 },
 {
  "sr.no.": 43,
  "Date": "25-Aug-18",
  "Particulars": "KTC Co.",
  "Address": "GE-3040,Bharat Diamond Bourse, Bandra Kurla Complex, Bandra East, Mumbai",
  "GSTIN\/UIN": "27AAGFK4725L1Z1",
  "QUantity": "1 Unit",
  "CONTACT NO.": 7852844301,
  "NAME": "Manish bhai"
 },
 {
  "sr.no.": 44,
  "Date": "25-Aug-18",
  "Particulars": "BHAVYA GEMS",
  "Address": "EW 5120,Bharat Diamond Bourse, G Block ,Bandra Kurla Complex, Bandra East, Mumbai",
  "GSTIN\/UIN": "27AABFB8758K1Z0",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820552032,
  "NAME": "devang parikh"
 },
 {
  "sr.no.": 45,
  "Date": "27-Aug-18",
  "Particulars": "Rusabh Diamonds",
  "Address": "CE - 2010,C - Tower, Bharat Diamond Bourse, Bandra Kurla Complex, Bandra (East), Mumbai",
  "GSTIN\/UIN": "27AAIFR7677Q1Z1",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9320075001,
  "NAME": "alpesh mehta"
 },
 {
  "sr.no.": 46,
  "Date": "11-Sep-18",
  "Particulars": "OVERSEAS GEMS",
  "Address": "4010, BHARAT DIAMOND BOURSE, BANDRA KURAL COMPLEX, BANDRA",
  "GSTIN\/UIN": "27AAEPS6925J1Z8",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9821026172,
  "NAME": "Vikram bhai"
 },
 {
  "sr.no.": 47,
  "Date": "11-Sep-18",
  "Particulars": "Kuber Diam",
  "Address": "DW 5240-50,G Block, Bharat Diamond Bourse, BKC, BANDRA, MUMBAI",
  "GSTIN\/UIN": "27AAOFK0817D1ZH",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9769116693,
  "NAME": "Satish bhai"
 },
 {
  "sr.no.": 48,
  "Date": "22-Sep-18",
  "Particulars": "Akshar Diamonds",
  "Address": "Bw-2020,Bharat Diamond Bourse, Bandra Kurla Complex,, Bandra (E), Mumbia",
  "GSTIN\/UIN": "27AAAFA6391C1ZQ",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820124178,
  "NAME": "Rohit bhai",
  "EMAIL ID": "aksharbw2020@gmail.com"
 },
 {
  "sr.no.": 49,
  "Date": "25-Sep-18",
  "Particulars": "S Jogani Exports Private Limited",
  "Address": "DW - 3010,D TOWER WEST WING, BHARAT DIAMOND BOURSE, BKC BANDRA (E), MUMBAI",
  "GSTIN\/UIN": "27AALCS4862J1ZS",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9920360074,
  "NAME": "Paresh bhai"
 },
 {
  "sr.no.": 50,
  "Date": "09-Oct-18",
  "Particulars": "Champa Lal Jewellers Private Limited",
  "Address": "1071-72,Maliwara, Chandni Chowk",
  "GSTIN\/UIN": "07AACCC5839L1ZC",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 51,
  "Date": "16-Oct-18",
  "Particulars": "C SPARKKLE",
  "Address": "55,6TH FLOOR,VASUNDHARA BUILDING, BHULABHAI DESAI ROAD, CUMBALA HILL, Mumbai",
  "GSTIN\/UIN": "27AXXPS2612Q1ZG",
  "QUantity": "1 Unit",
  "CONTACT NO.": "022-3392 3213",
  "NAME": "VISHAL SHAH",
  "EMAIL ID": "csparkkleinfo@gmail.com"
 },
 {
  "sr.no.": 52,
  "Date": "25-Oct-18",
  "Particulars": "MANAV GEMS",
  "Address": "The Capital,910, 9th Floor, C-70,, G-Block, Bandra Kurla Complex,, Bandra (E), Mumbai",
  "GSTIN\/UIN": "27AAOFM2587N1ZF",
  "QUantity": "1 Unit",
  "CONTACT NO.": 2267102270,
  "NAME": "Manav gems"
 },
 {
  "sr.no.": 53,
  "Date": "27-Oct-18",
  "Particulars": "Rudra Export",
  "Address": "JE-5240,Bharat Diamond Bourse, BKC, Bandra(East), Mumbai",
  "GSTIN\/UIN": "27AANFR2426C1ZC",
  "QUantity": "1 Unit",
  "CONTACT NO.": 7567333888,
  "NAME": "vishalkumar G patel",
  "EMAIL ID": "rudragemssurat@gmail.com"
 },
 {
  "sr.no.": 54,
  "Date": "29-Oct-18",
  "Particulars": "Grace Jewels Pvt. Ltd.",
  "Address": "A 45, VIRWANI INDUSTRIAL ESTATE, OFF WESTERN EXPRESS HIGHWAY, GOREGAON (EAST), MUMBAI",
  "GSTIN\/UIN": "27AACCG2538G1ZR",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 55,
  "Date": "26-Nov-18",
  "Particulars": "JAY GEMS",
  "Address": "403 D,4th Floor Green Wood, Andheri Kurla Rd,Chakala, Andheri - E, Mumbai Zone -3",
  "GSTIN\/UIN": "27AELPP3834Q1ZO",
  "QUantity": "1 Unit",
  "CONTACT NO.": -9328104936,
  "NAME": "JERAMBHAI LAVJIBHAI DONDA",
  "EMAIL ID": "jay_gemss@yahoo.co.in"
 },
 {
  "sr.no.": 56,
  "Date": "26-Nov-18",
  "Particulars": "M\/s. Khushi Gems",
  "Address": "Cc-39,Bharat Diamond Bourse, BKC, Bandra(E), Mumbai",
  "GSTIN\/UIN": "27AAMFK7662A1Z8",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 57,
  "Date": "04-Dec-18",
  "Particulars": "M Shailesh & Co.",
  "Address": "GE-4042, G Block Bharat Diamond Bourse, Bandra Kurla Complex,Bandra (E), Mumbai",
  "GSTIN\/UIN": "27AAEFM6829P1ZK",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820235645,
  "NAME": "Shailesh A Shah",
  "EMAIL ID": "msmumbai@hotmail.com"
 },
 {
  "sr.no.": 58,
  "Date": "06-Dec-18",
  "Particulars": "ACME DIAMOND EXPORTS PRIVATE LIMITED",
  "Address": "AW 6040, A TOWER WEST CORE, BDD BKC, BANDRA, Mumbai",
  "GSTIN\/UIN": "27AAECA9490P1ZV",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9833485490,
  "NAME": "Ganpat bhai"
 },
 {
  "sr.no.": 59,
  "Date": "20-Dec-18",
  "Particulars": "VARNI GEMS",
  "Address": "1, EE-1011, TOWER-E,, BHARAT DIAMOND BOURSE, BANDRA KURLA COMPLEX, BANDRA EAST",
  "GSTIN\/UIN": "27AACFV2716Q1ZP",
  "QUantity": "1 Unit",
  "NAME": "Kunal"
 },
 {
  "sr.no.": 60,
  "Date": "22-Dec-18",
  "Particulars": "Ashish Impex",
  "Address": "402,Orion Business Park,, Nehru Road,Santacruz(East), Mumbai",
  "GSTIN\/UIN": "27AAFFA6111K1ZM",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820152691,
  "NAME": "hitesh bhai"
 },
 {
  "sr.no.": 61,
  "Date": "05-Jan-19",
  "Particulars": "Swet Gems",
  "Address": "FW-5040,5th Floor,Bharat Diamond Bourse,, Bandra Kurla Complex,Bandra (E), Mumbai",
  "GSTIN\/UIN": "27AAAFS6863R1ZC",
  "QUantity": "1 Unit",
  "CONTACT NO.": 26721400,
  "NAME": "devshibhai dunrani",
  "EMAIL ID": "swetgems@gmail.com"
 },
 {
  "sr.no.": 62,
  "Date": "07-Jan-19",
  "Particulars": "Sanskar Gems",
  "Address": "Flat No.51,Clover Park CHS Ltd., Plot No.46,TPS 6, Lalubhai Park, Andheri West, Greater Mumbai",
  "GSTIN\/UIN": "27ABCFS8324C1ZB",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 63,
  "Date": "18-Jan-19",
  "Particulars": "Johari & Sons",
  "Address": "CC - 3020,Bharat Diamond Bourse, Bandra Kurla Complex, Bandra West, Mumbai",
  "GSTIN\/UIN": "27AANFJ3843R1ZI",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9867825693,
  "EMAIL ID": "johariandsons@gmail.com"
 },
 {
  "sr.no.": 64,
  "Date": "18-Jan-19",
  "Particulars": "kikani Gems (Surat)",
  "Address": "DC-3180,Bharat Diamond Bourse, Bandra Kurla Complex,, Bandra (E), Mumbai",
  "GSTIN\/UIN": "27AAKFK0018N1Z7",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 65,
  "Date": "18-Jan-19",
  "Particulars": "H K DIAM JEWELLERY LLP",
  "Address": "2A-26,ASHIRWAD BLDG.,ASHA NAGAR, THAKUR COMPLEX, KANDIWALI EAST, MUMBAI",
  "GSTIN\/UIN": "27AAKFH0093E1ZI",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9326729627,
  "NAME": "Nakul bhai"
 },
 {
  "sr.no.": 66,
  "Date": "18-Jan-19",
  "Particulars": "Somira Diam Private Limited",
  "Address": "C\/401,New Sarvottam CHSL,, S V Road, Near Irla Bridge, Andheri, Mumbai Sunburn",
  "GSTIN\/UIN": "27AAWCS9138A1ZX",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 67,
  "Date": "02-Feb-19",
  "Particulars": "VRP Diamonds LLP",
  "Address": "209\/10,Shreeji Chambers, 2nd Floor Prasad Chambers, Opera House, Mumbai",
  "GSTIN\/UIN": "27AAOFV3684K1ZC",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 68,
  "Date": "02-Feb-19",
  "Particulars": "Purvi Enterprise",
  "Address": "FC 8061-62,Bharat Diamond Bourse, Bandra Kurla Complex, Bandra East, Mumbai",
  "GSTIN\/UIN": "27AAEFP2925M1ZY",
  "QUantity": "1 Unit",
  "CONTACT NO.": 7900089867,
  "NAME": "pankaj"
 },
 {
  "sr.no.": 69,
  "Date": "02-Feb-19",
  "Particulars": "Shah Brothers Diamonds Pvt Ltd.",
  "Address": "GE-2041-42,Bharat Diamonds Bourse, Bandra Kurla Complex, Bandra (East), Mumbai",
  "GSTIN\/UIN": "27AACCD9837F1ZG",
  "QUantity": "1 Unit",
  "EMAIL ID": "shahbrothers14@gmail.com"
 },
 {
  "sr.no.": 70,
  "Date": "04-Feb-19",
  "Particulars": "Hiral Exports",
  "Address": "6th,DW 6160 G Block D Tower, Bharat Diamond Bourse, Bandra Kurla Complex, Bandra(E), Mumbai",
  "GSTIN\/UIN": "27AACFH3237N1Z7",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 71,
  "Date": "05-Feb-19",
  "Particulars": "Mitu Export",
  "Address": "DE-5120,Bharat Diamond Bourse, BKC - G Block, Bandra East, Mumbai",
  "GSTIN\/UIN": "27AANPS9721K1ZX",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9702021064,
  "NAME": "kaushik shah"
 },
 {
  "sr.no.": 72,
  "Date": "05-Feb-19",
  "Particulars": "Aloma Diamond Private Limited",
  "Address": "A\/102 Mahavir Villa ,Sai Nagar, Vasai Road West, Palghar",
  "GSTIN\/UIN": "27AARCA0244N1ZC",
  "QUantity": "2 Unit",
  "CONTACT NO.": 7021180889,
  "NAME": "Amishkumar",
  "EMAIL ID": "shaileshrikame23@gmail.com"
 },
 {
  "sr.no.": 73,
  "Date": "12-Mar-19",
  "Particulars": "Akhand Anand Exports",
  "Address": "C\/46,3rd Floor,Tarabaug Estate, R R Roi Marg, Mumbai, 400004",
  "GSTIN\/UIN": "27AAJFA4787B1ZF",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9619011718,
  "NAME": "Prakash bhai",
  "EMAIL ID": "akhandanandexports@gmail.com"
 },
 {
  "sr.no.": 74,
  "Date": "12-Mar-19",
  "Particulars": "Nine Diamonds",
  "Address": "1119, Prasad Chambers, Opera House, Mumbai",
  "GSTIN\/UIN": "27AACPS6836J1Z8",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 75,
  "Date": "13-Mar-19",
  "Particulars": "Mansi Gems",
  "Address": "2,205,Meghdoot Chsl,, Raheja Township, Malad East, Mumbai",
  "GSTIN\/UIN": "27AAQFM8110P1ZM",
  "QUantity": "1 Unit",
  "CONTACT NO.": 7400206267,
  "NAME": "sagar bhai"
 },
 {
  "sr.no.": 76,
  "Date": "13-Mar-19",
  "Particulars": "Dhanera Diamonds",
  "Address": "GW-5010-21-22-23,Bharat Diamond Bourse, Bandra Kurla Complex,, Bandra (East)",
  "GSTIN\/UIN": "27AAAFD0634K1ZO",
  "QUantity": "1 Unit",
  "CONTACT NO.": "91 22 6789171.1",
  "NAME": "danera",
  "EMAIL ID": "lnfo@dhaneradiamonds .com "
 },
 {
  "sr.no.": 77,
  "Date": "14-Mar-19",
  "Particulars": "Kora Diamonds LLP",
  "Address": "BC 4022B,Bharat Diamond Bourse, Bandra Kurla Complex, Bandra East, Mumbai",
  "GSTIN\/UIN": "27AAPFK4795H1ZN",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 78,
  "Date": "19-Mar-19",
  "Particulars": "Subh Diam",
  "Address": "DW-6020,Bharat Diamond Bourse, Bandra Kurla Complex, Bandra(E), Mumbai",
  "GSTIN\/UIN": "27ACXFS7497N1ZL",
  "QUantity": "2 Unit"
 },
 {
  "sr.no.": 79,
  "Date": "29-Mar-19",
  "Particulars": "MBK Gems",
  "Address": "1st Floor, Office No-116, Panch Ratna Diamond Hall, Mohan Nagar, Mini Bazar, Varaccha, Surat",
  "GSTIN\/UIN": "24ABAFM1925H1ZM",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 80,
  "Date": "30-Mar-19",
  "Particulars": "Dharam Gems",
  "Address": "DW 3370, Bharat Diamond Bourse, Bandra Kurla Complex, Bandra ( E ), Mumbai",
  "GSTIN\/UIN": "27APYPS9195K1ZF",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820077740,
  "NAME": "Dharam bhai"
 },
 {
  "sr.no.": 81,
  "Date": "10-Apr-19",
  "Particulars": "Shine Star",
  "Address": "BW 3031\/3032, Bharat Diamond Bourse, Bandra Kurla Complex, Bandra East, Mumbai",
  "GSTIN\/UIN": "27AABFS2911F1ZJ",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820388816,
  "NAME": "shubhash shah",
  "EMAIL ID": "shinestar916@yahoo.com"
 },
 {
  "sr.no.": 82,
  "Date": "10-Apr-19",
  "Particulars": "JANAM DIAMONDS PVT LTD",
  "Address": "3RD FLOOR, DW 3301, BHARAT DIAMOND BOURSE, BANDRA KURLA COMPLEX, BANDRA, Mumbai City,",
  "GSTIN\/UIN": "27AAACJ0950D1Z0",
  "QUantity": "1 Unit",
  "CONTACT NO.": 7790,
  "NAME": "janam diamond"
 },
 {
  "sr.no.": 83,
  "Date": "10-Apr-19",
  "Particulars": "Pranami Gems",
  "Address": "CC 7084 Bharat Diamond Bourse, Bandra Kurla Complex, Bandra, Mumbai",
  "GSTIN\/UIN": "27AAAFP1746L1Z3",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9821183770,
  "NAME": "haribhai j patel",
  "EMAIL ID": "pranamigem@gmail.com"
 },
 {
  "sr.no.": 84,
  "Date": "10-Apr-19",
  "Particulars": "MARUTI DIAMONDS",
  "Address": "601 A WING, KALPAANA CHS LTD,, 20 PARK ROAD, VILE \nPARLE EAST,, Mumbai Suburban,",
  "GSTIN\/UIN": "27AAAFM0408Q1Z7",
  "QUantity": "1 Unit",
  "CONTACT NO.": "022-40056734",
  "NAME": "Sanjay Mendpara",
  "EMAIL ID": "marutidiamonds6734@gmail.com"
 },
 {
  "sr.no.": 85,
  "Date": "10-Apr-19",
  "Particulars": "MIRAJ GEMS",
  "Address": "602,SATAYAPRASAD APT, DIXIT CROSS ROADNO.1, VILE PARLE(E) MUMBAI-400057",
  "GSTIN\/UIN": "27AAGFM2748H1Z5",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9167064635,
  "NAME": "rishi bhai"
 },
 {
  "sr.no.": 86,
  "Date": "10-Apr-19",
  "Particulars": "Hari Darshan Exports Pvt.Ltd",
  "Address": "FC 4070, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East), Mumbai - 400 051.",
  "GSTIN\/UIN": "27AADCH3780N1Z4",
  "QUantity": "1 Unit",
  "CONTACT NO.": "7211\/9429075100",
  "NAME": "jay bhai"
 },
 {
  "sr.no.": 87,
  "Date": "10-Apr-19",
  "Particulars": "Bhadiyadra Gems",
  "Address": "Office No-1, Shreeji Plaza, 1st Floor, Tata Road No-1, Opera House, Mumbai",
  "GSTIN\/UIN": "27AAAFB1561H1ZT",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9819897971,
  "NAME": "Mukesh bhai",
  "EMAIL ID": "bhadiyadragems@gmail.com"
 },
 {
  "sr.no.": 88,
  "Date": "25-Apr-19",
  "Particulars": "S.M.Diamonds",
  "Address": "GE-9110, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East), Mumbai - 400 051",
  "GSTIN\/UIN": "27ADWPS1634F1Z5",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 89,
  "Date": "25-Apr-19",
  "Particulars": "Rikin Diam",
  "Address": "401, Rajni Mahel Apt., Tardeo Road,, Tardeo, Mumbai - 400 034",
  "GSTIN\/UIN": "27BFVPS2639E1ZW",
  "QUantity": "1 Unit",
  "CONTACT NO.": 8080447446,
  "NAME": "Mitesh shah"
 },
 {
  "sr.no.": 90,
  "Date": "25-Apr-19",
  "Particulars": "Lightex",
  "Address": "AE-5070, Bharat Diamond Bourse,, Bandra Kurla Complex, Bandra (East),, Mumbai - 400 051",
  "GSTIN\/UIN": "27AAAFL0451G1ZQ",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9821028010,
  "NAME": "Ajay bhai"
 },
 {
  "sr.no.": 91,
  "Date": "25-Apr-19",
  "Particulars": "Kikani Gems (Surat)",
  "Address": "HN NO 1987\/88, OFFICE NO 301,304,306,307,, KABIR COMPLEX, DALGIYA STREET,, MAHIDHARPURA, SURAT",
  "GSTIN\/UIN": "24AAKFK0018N1ZD",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 92,
  "Date": "25-Apr-19",
  "Particulars": "ANU GEMS",
  "Address": "6\/1909,202 Ambika Building, Jadakhadi, Mahidharpura, Surat",
  "GSTIN\/UIN": "24AALFA2752L1ZD",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 93,
  "Date": "30-May-19",
  "Particulars": "Aaryan International",
  "Address": "DW 4021, BHARAT DIAMOND BOURSE, BANDRA KURLA COMPLEX,, BANDRA EAST,, MUMBAI",
  "GSTIN\/UIN": "27AAZFA6534E1Z4",
  "QUantity": "1 Unit",
  "NAME": "pg shah",
  "EMAIL ID": "pgshah75@gmail.com"
 },
 {
  "sr.no.": 94,
  "Date": "30-May-19",
  "Particulars": "Khodal Gems",
  "Address": "AE 3071\/72 BHARAT DIAMOND BOURSE, BANDRA KURLA COMPLEX, BANDRA EAST, MUMBAI",
  "GSTIN\/UIN": "27AAAFK6912F1ZJ",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9029312839,
  "NAME": "tushar bhai"
 },
 {
  "sr.no.": 95,
  "Date": "30-May-19",
  "Particulars": "Siddhi Gems",
  "Address": "B\/1701, Wing B, Rustomjee Paramount, JN Ramkrishna Mission Road and 18th Road, Khar West, Mumbai",
  "GSTIN\/UIN": "27AKVPS5306G1ZO",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 96,
  "Date": "31-May-19",
  "Particulars": "D Chhaganlal & Co",
  "Address": "EW-1040\/50 BHARAT DIAMOND BOURSE, BANDRA KURLA COMPLEX, BANDRA ( E ), MUMBAI",
  "GSTIN\/UIN": "27AAAFD1578Q1ZZ",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 97,
  "Date": "03-Jun-19",
  "Particulars": "Kaka Diam",
  "Address": "EC 1090, Bharat Diamond Bourse, Bandra Kurla Complex, Bandra East, Mumbai",
  "GSTIN\/UIN": "27AAIFK7398F1ZT",
  "QUantity": "1 Unit",
  "CONTACT NO.": 7825,
  "NAME": "QBC Kaka diam"
 },
 {
  "sr.no.": 98,
  "Date": "04-Jun-19",
  "Particulars": "Dimexon Diamonds Ltd.",
  "Address": "401-403\/ Diamoda Unit, Novelty Silk Mill Compound, Dahisar ( E ), Mumbai",
  "GSTIN\/UIN": "27AAACD1877D1ZU",
  "QUantity": "2 Unit"
 },
 {
  "sr.no.": 99,
  "Date": "08-Jun-19",
  "Particulars": "Rinkle Impex",
  "Address": "FW 3200, Bharat Diamond Bourse, Bandra Kurla Complex,, Bandra ( East ), Mumbai",
  "GSTIN\/UIN": "27AAEFR6271N1ZN",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 100,
  "Date": "11-Jul-19",
  "Particulars": "B G Star Diamond",
  "Address": "A\/505, BLDG No.2, Patidar CHS Ltd.,, Shrarda Nagar, S V Road, Plot No.21,, Malad (West), Mumbai - 400 064",
  "GSTIN\/UIN": "27AAHFB7686G1Z2",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 101,
  "Date": "11-Jul-19",
  "Particulars": "ANSHU EXPORTS \n",
  "Address": "7TH, 702, SATYA PRASAD CHS LTD, DIXIT CROSS ROAD, VILE PARLE EAST,, Mumbai - 400 057",
  "GSTIN\/UIN": "27AAOFA4633K1Z6",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 102,
  "Date": "12-Jul-19",
  "Particulars": "Party Impex",
  "Address": "401\/A, Priti Palace, D.N.Cross Road No.3,, Vile Parle (West),, Mumbai - 400 056",
  "GSTIN\/UIN": "27AAEFP2830R1ZS",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9322445772,
  "NAME": "party impex"
 },
 {
  "sr.no.": 103,
  "Date": "15-Jul-19",
  "Particulars": "Sejal Gems",
  "Address": "201,205, Navpad,Jadakhadi,, Mahidharpura, Sutat- 395 003",
  "GSTIN\/UIN": "24AAKFS9077MIZE",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9619652562,
  "NAME": "Vanita madam"
 },
 {
  "sr.no.": 104,
  "Date": "23-Jul-19",
  "Particulars": "Goldiam International Ltd",
  "Address": "11th Floor, The Capital, Office No. 1107,, A Wing, Plot No.C 70 G Block,, Bandra Kurla Complex, Bandra (East),, Mumbai -400 051",
  "GSTIN\/UIN": "27AAACG2271J2ZN",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9619724915,
  "NAME": "Goldiam"
 },
 {
  "sr.no.": 105,
  "Date": "26-Jul-19",
  "Particulars": "Amrut Gems",
  "Address": "EC 6070, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East), Mumbai - 400 051",
  "GSTIN\/UIN": "27AADFA1157D1ZZ",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9967520251,
  "NAME": "Vipul bhai"
 },
 {
  "sr.no.": 106,
  "Date": "09-Aug-19",
  "Particulars": "Shairu Gems Diamonds Private Limited",
  "Address": "DE-9012-A, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra(East),, Mumbai",
  "GSTIN\/UIN": "27AATCS5148R1Z7",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 107,
  "Date": "16-Aug-19",
  "Particulars": "Vikas Gems",
  "Address": "DC-6030\/40, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AACFV2553P1ZO",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9920968368,
  "NAME": "suresh bhai"
 },
 {
  "sr.no.": 108,
  "Date": "21-Aug-19",
  "Particulars": "Ariha Diamonds",
  "Address": "404, Kanakshanti, Opp. Diamond Village,, Jadakhadi, Mahidharpura,, Surat - 395 003, CONT NO.:- 0261-3009159",
  "GSTIN\/UIN": "24ABHFA2488A1ZT",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 109,
  "Date": "04-Sep-19",
  "Particulars": "Nirbhay Gems",
  "Address": "BW-9030, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAIFN6515H1Z5",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 110,
  "Date": "30-Sep-19",
  "Particulars": "Tulip Exports",
  "Address": "DC-1150 A, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAIFT9668B1ZR",
  "QUantity": "1 Unit",
  "CONTACT NO.": 8879073912,
  "NAME": "Satish bhai"
 },
 {
  "sr.no.": 111,
  "Date": "01-Oct-19",
  "Particulars": "Decent Star",
  "Address": "DE-3200, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAGFD6278H1Z5",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 112,
  "Date": "08-Oct-19",
  "Particulars": "Sara Diamonds Private Limited",
  "Address": "GW-4010, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai- 400051.",
  "GSTIN\/UIN": "27AARCS6939C1ZV",
  "QUantity": "1 Unit",
  "CONTACT NO.": 45200022,
  "NAME": "meet shah",
  "EMAIL ID": "sales@saradiamonds.com"
 },
 {
  "sr.no.": 113,
  "Date": "22-Oct-19",
  "Particulars": "Birani Impex",
  "Address": "JE-5160, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27BUUPB8991G1ZW",
  "QUantity": "1 Unit",
  "CONTACT NO.": 7507052771,
  "NAME": "sandeep bhai"
 },
 {
  "sr.no.": 114,
  "Date": "16-Nov-19",
  "Particulars": "Rutva Gems",
  "Address": "4\/19 Elephanta CHS,, Gaushala Lane,Daftary Road,, Malad (East),, Mumbai",
  "GSTIN\/UIN": "27AASFR2682K1ZG",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 115,
  "Date": "22-Nov-19",
  "Particulars": "Karni Jewellers",
  "Address": "3-5-997-1, Narayanaguda,, Hyderabad",
  "GSTIN\/UIN": "36AADFK5720G1ZJ",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 116,
  "Date": "07-Dec-19",
  "Particulars": "Angira Gems",
  "Address": "229, Panchratna,, M. P. Marg,, Opera House,, Mumbai",
  "GSTIN\/UIN": "27AFFPP0234D1ZV",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 117,
  "Date": "28-Dec-19",
  "Particulars": "Aum Star",
  "Address": "FW 28, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAOFA7670G1Z4",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 118,
  "Date": "02-Jan-20",
  "Particulars": "Pearl Diam",
  "Address": "BE-1140, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27ARVPK5166D1ZE",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 119,
  "Date": "04-Jan-20",
  "Particulars": "Katariya Lalji Maganbhai",
  "Address": "19, Anand Dhan Complex,, Near Bus Stand,, Mahuva",
  "QUantity": "2 Unit",
  "CONTACT NO.": 9725388848,
  "NAME": "Lalji bhai"
 },
 {
  "sr.no.": 120,
  "Date": "17-Jan-20",
  "Particulars": "Miraj Gems",
  "Address": "602, Satyaprasad Apartment,, Dixit Cross Road No.1,, VileParle (East),, Mumbai",
  "GSTIN\/UIN": "27AAGFM2748H1Z5",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9167064635,
  "NAME": "rishi bhai"
 },
 {
  "sr.no.": 121,
  "Date": "18-Jun-20",
  "Particulars": "Nilkanth Gems",
  "Address": "3RD FLOOR, 305, NEW PATIDAR BHAVAN, HIRA BAZAR, MAHIDHARPURA,, Surat, Gujarat, 395003 \n",
  "GSTIN\/UIN": "24AAHFN6822G1ZC",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9619797631,
  "NAME": "jg gadhya"
 },
 {
  "sr.no.": 122,
  "Date": "01-Aug-20",
  "Particulars": "M.R. Diamond",
  "Address": "Plot No. 4 to 7, 31-32, Kumbhar Faliyu,, Nr. Peoples Char Rasta,, Gotalwadi. Katargam,, Surat",
  "GSTIN\/UIN": "24ABBFM3714H1ZM",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 123,
  "Date": "01-Aug-20",
  "Particulars": "Anand Exports",
  "Address": "DW-1090,BHARAT DIAMOND BOURSE,, BANDRA KURLA COMPLEX,, BANDRA(E), MUMBAI",
  "GSTIN\/UIN": "27AAHFA4063C1ZU",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 124,
  "Date": "15-Sep-20",
  "Particulars": "Golwala",
  "Address": "GW-6023, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra(East),, Mumbai",
  "GSTIN\/UIN": "27AAEFR4075N1ZP",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9136234687,
  "NAME": "Atma ram bhai"
 },
 {
  "sr.no.": 125,
  "Date": "15-Sep-20",
  "Particulars": "J.K. Star",
  "Address": "GE-6051, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra(East),, Mumbai",
  "GSTIN\/UIN": "27AAAFJ1770G1ZK",
  "QUantity": "1 Unit",
  "CONTACT NO.": 7756830118,
  "NAME": "Naresh bhai"
 },
 {
  "sr.no.": 126,
  "Date": "15-Sep-20",
  "Particulars": "Jay Gems",
  "Address": "905 Princess Plaza,, Varacha Road, Surat,, Gujrat - 395 006",
  "GSTIN\/UIN": "24AELPP3834Q1ZU",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9328105027,
  "NAME": "jerambhai lavjibhai",
  "EMAIL ID": "jay_gemss@yahoo.co.in"
 },
 {
  "sr.no.": 127,
  "Date": "17-Oct-20",
  "Particulars": "MAHENDRA BROTHERS EXPORTS PVT. LTD.",
  "Address": "G - BLOCK, 7TH FLOOR, CE-7011, CE-7012, CE-7013,, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAFCM0246E1ZT",
  "QUantity": "1 Unit",
  "CONTACT NO.": 8900145642,
  "NAME": "mahindra brother kkaka"
 },
 {
  "sr.no.": 128,
  "Date": "14-Dec-20",
  "Particulars": "Neelkanth Gems",
  "Address": "605, Vastushilp Apartment,, Near Parsi Colony Pump House,, Andheri (East),, Mumbai",
  "GSTIN\/UIN": "27AAAFH0191F1ZR",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9619797631,
  "NAME": "jg gadhya"
 },
 {
  "sr.no.": 129,
  "Date": "17-Dec-20",
  "Particulars": "Yovan Impex",
  "Address": "105, Sagar Building, 1st Floor, 39 Dr Deshmukh Lane,, V.P.Road,, Mumbai-400004",
  "GSTIN\/UIN": "27AABFY4209N1ZT",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 130,
  "Date": "25-Dec-20",
  "Particulars": "Padmavati Exports",
  "Address": "FW-7021\/22, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra(East),, Mumbai",
  "GSTIN\/UIN": "27AADFP2474Q1ZN",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9987242600,
  "NAME": "Aarti"
 },
 {
  "sr.no.": 131,
  "Date": "27-Jan-21",
  "Particulars": "Kush Impex",
  "Address": "43, Shreeji Plaza,, Tata Road No.1,, Opera House,, Mumbai",
  "GSTIN\/UIN": "27AADFK5279J1ZX",
  "QUantity": "1 Unit",
  "CONTACT NO.": 8860282945,
  "NAME": "khush"
 },
 {
  "sr.no.": 132,
  "Date": "27-Jan-21",
  "Particulars": "Yug Global Private Limited",
  "Address": "6th Floor, 602, Abrol Windsor,, Upper Govind Nagar,, Nandkumar Kale Bunglow,, Malad (East),, Mumbai",
  "GSTIN\/UIN": "27AABCY2031K1ZD",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 133,
  "Date": "27-Jan-21",
  "Particulars": "R.C. Gems",
  "Address": "B\/603, Charmee Enclave,, Shraddhanand Service Road,, Vile Parle (East),, Mumbai",
  "GSTIN\/UIN": "27AADFR8460J1ZT",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 134,
  "Date": "02-Mar-21",
  "Particulars": "Samkit Diamond Export Pvt. Ltd.",
  "Address": "1st Floor, 111, Prasad Chambers,, Tata Raod No.2,, Opera House,, Mumbai",
  "GSTIN\/UIN": "27AATCS0381C1Z9",
  "QUantity": "1 Unit",
  "CONTACT NO.": 2233929599,
  "NAME": "Abhishek bhai"
 },
 {
  "sr.no.": 135,
  "Date": "31-Mar-21",
  "Particulars": "Khushbu Diamonds",
  "Address": "501,\"C\" Wing,Tulsi Villa,, Bajaj Road,, Vile Parle (West),, Mumbai",
  "GSTIN\/UIN": "27AAFFK1581M1Z0",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 136,
  "Date": "01-Apr-21",
  "Particulars": "Krishna Export",
  "Address": "EW-3030, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra(East),, Mumbai",
  "GSTIN\/UIN": "27AAAFK2239H1ZJ",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 137,
  "Date": "01-Apr-21",
  "Particulars": "Goti Exports",
  "Address": "502, 5th Floor, Rajshree Amber Building,, Upper Govind Nagar,, Malad (East),, Mumbai",
  "GSTIN\/UIN": "27AACFG7212J1ZH",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 138,
  "Date": "01-Apr-21",
  "Particulars": "Suraj Exports",
  "Address": "DE 8011\/12\/13, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra(East),, Mumbai",
  "GSTIN\/UIN": "27AAAFS3513J1ZB",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9320845403,
  "NAME": "Ganesh bhai"
 },
 {
  "sr.no.": 139,
  "Date": "03-Apr-21",
  "Particulars": "Sri Siddi Vinayak Jewellers & Exports Pvt. Ltd.",
  "Address": "3-6-97,G-4, Ihsan Surabhi Apartment,, Basheerbagh,, Hyderabad,, Telangana,",
  "GSTIN\/UIN": "36ABDCS1885L1ZU",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 140,
  "Date": "04-Jun-21",
  "Particulars": "Laxmi Dia Jewel Pvt. Ltd.",
  "Address": "Plot No.4, B.M.C. Industrail Estate,, M.G. Cross Road, No.1,, Sai Nagar, Kandivali(W),, Mumbai",
  "GSTIN\/UIN": "27AAACL8548B1ZK",
  "QUantity": "1 Unit",
  "CONTACT NO.": 8850300273,
  "NAME": "Shubam"
 },
 {
  "sr.no.": 141,
  "Date": "04-Jun-21",
  "Particulars": "Abhinandan Diamond",
  "Address": "38-C, Allakarkha Bldg;, Khetwadi 9th Lane,, Khetwadi,, Mumbai",
  "GSTIN\/UIN": "27AXOPS9848P1ZZ",
  "QUantity": "1 Unit",
  "CONTACT NO.": 8655118902,
  "NAME": "Nilesh bhai"
 },
 {
  "sr.no.": 142,
  "Date": "04-Jun-21",
  "Particulars": "Alpesh Diamond",
  "Address": "CC-5011, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai-400 051.",
  "GSTIN\/UIN": "27AAAFA6852E1ZO",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 143,
  "Date": "04-Jun-21",
  "Particulars": "S. Jogani Impex",
  "Address": "DW-3180, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27ADTFS2109Q1ZA",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9920360074,
  "NAME": "paresh bhai"
 },
 {
  "sr.no.": 144,
  "Date": "04-Jun-21",
  "Particulars": "Fancy diamonds",
  "Address": "GE-2031, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAAFF0229L1ZL",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 145,
  "Date": "26-Jun-21",
  "Particulars": "freinds International",
  "Address": "AE-7080, Bharat Diamond Bourse,, Bandra Kurla Complex,, Mumbai",
  "GSTIN\/UIN": "27AAYCS7080B1ZW",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 146,
  "Date": "26-Jun-21",
  "Particulars": "Diaglow Gems Private Limited",
  "Address": "GE-8031\/32, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai-400 051.",
  "GSTIN\/UIN": "27AAOCS9609Q1Z8",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 147,
  "Date": "26-Jun-21",
  "Particulars": "Beauty Creation Private Limited",
  "Address": "26th Floor, 262, Rushabh Apartment,, Dr. Parekh Street,, Parthana Samaj,, Girgaon,, Mumbai",
  "GSTIN\/UIN": "27AABCV8888K1ZF",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 148,
  "Date": "26-Jun-21",
  "Particulars": "Twara Diam",
  "Address": "BH, Gurukul,1593A, Marine Society,, Sardarnagar,, Bhavnagar",
  "GSTIN\/UIN": "24AAJFT3313N1Z1",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9824402263,
  "NAME": "vikash bhai"
 },
 {
  "sr.no.": 149,
  "Date": "28-Jun-21",
  "Particulars": "Aneri Jewels",
  "Address": "307, RASHMI ENCLAVE-A-CHS LTD.,, Shanti Park,Nr.ST.Xaviers School,, Mira Road(East),, Thane",
  "GSTIN\/UIN": "27AUGPP9723M1ZW",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820436789,
  "NAME": "Amit bhai",
  "EMAIL ID": "anerijewels@gmail.com"
 },
 {
  "sr.no.": 150,
  "Date": "25-Sep-21",
  "Particulars": "Aum Star -Surat",
  "Address": "3rd Floor, Plot No. 14 to 16, Danev Estate B,, Sarathi Industrial Estate,, Vasta Devdi Road,, Katargam,, Surat",
  "GSTIN\/UIN": "24AAOFA7670G1ZA",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 151,
  "Date": "06-Oct-21",
  "Particulars": "KGK DIAMONDS (I) PRIVATE LIMITED",
  "Address": "DE-4011-4016, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AADCK7579A1ZF",
  "QUantity": "2 Unit",
  "CONTACT NO.": 9619188933,
  "NAME": "piyush"
 },
 {
  "sr.no.": 152,
  "Date": "06-Oct-21",
  "Particulars": "R.Rajesh Exports",
  "Address": "EW-5181-82-83, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAAFR0336G1ZK",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820040669,
  "NAME": "hitakshi shah"
 },
 {
  "sr.no.": 153,
  "Date": "06-Oct-21",
  "Particulars": "R.Chirag & Co.",
  "Address": "1702, Rushabh Apartment,, Parekh Street,, Parthana Samaj, Mumbai",
  "GSTIN\/UIN": "27AAHFR2830G1ZA",
  "QUantity": "1 Unit",
  "CONTACT NO.": 8291722945,
  "NAME": "dev panja"
 },
 {
  "sr.no.": 154,
  "Date": "07-Oct-21",
  "Particulars": "Maniya Exim",
  "Address": "1st Floor, Office No. 178,, Sardar Diamond Market-1,, Varaccha Road,, Mini Bazar,, Surat",
  "GSTIN\/UIN": "24ASQPM4822N1Z7",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9967979956,
  "NAME": "Ritesh"
 },
 {
  "sr.no.": 155,
  "Date": "03-Dec-21",
  "Particulars": "KGK DIAMONDS (I) PRIVATE LIMITED",
  "Address": "DE-4011-4016, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AADCK7579A1ZF",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9619188933,
  "NAME": "piyush"
 },
 {
  "sr.no.": 156,
  "Date": "03-Dec-21",
  "Particulars": "S. Jogani Impex",
  "Address": "DW-3180, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27ADTFS2109Q1ZA",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9920360074,
  "NAME": "paresh mheta"
 },
 {
  "sr.no.": 157,
  "Date": "03-Dec-21",
  "Particulars": "Rose Gems",
  "Address": "GE-5070, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AADFR4361G1Z8",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9221832802,
  "NAME": "Ram Chandra bhai",
  "EMAIL ID": "rosegems1995@gmail.com"
 },
 {
  "sr.no.": 158,
  "Date": "03-Dec-21",
  "Particulars": "Laxmi Enterprise",
  "Address": "101, Laxmi Narayan Building,, Bhojabhai Ni Tekaro,, Dalagiya Mohollo,, Mahidharpura,, Surat",
  "GSTIN\/UIN": "24AAJPV5069R1ZP",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 159,
  "Date": "06-Dec-21",
  "Particulars": "Suraj Diamond",
  "Address": "A-108-109, 1st Floor, Diamond Village,, Jadakhadi,, Mahidharpura,, Surat",
  "GSTIN\/UIN": "24ABGFS3708Q1ZQ",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 160,
  "Date": "20-Jan-22",
  "Particulars": "Freinds International",
  "Address": "Devi Path, B-48,, J.L.N. Marg,, Jaipur",
  "GSTIN\/UIN": "08AAAFF8947M1ZU",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 161,
  "Date": "20-Jan-22",
  "Particulars": "Ultimate Creation Private Limited",
  "Address": "1st Floor, Plot No.96,, Opp. Hotel Suncity,, Midc, Road No.16,, Andheri (East),, Mumbai",
  "GSTIN\/UIN": "27AACCU9352Q1ZI",
  "QUantity": "1 Unit",
  "CONTACT NO.": "98204 60204",
  "NAME": "Parth Kunjadiya.",
  "EMAIL ID": "parthkunjadiya@gmail.com"
 },
 {
  "sr.no.": 162,
  "Date": "22-Jan-22",
  "Particulars": "P. Hitesh & Co.",
  "Address": "4th Floor, Akshay Raj Building,, Jadakhadi,, Mahidharpura,, Surat,",
  "GSTIN\/UIN": "24AADFP7770K1ZW",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 163,
  "Date": "01-Feb-22",
  "Particulars": "Rasikllal and Sons",
  "Address": "BC-5010\/B2, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAAFR0937K1Z4",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9821039558,
  "NAME": "Samir",
  "EMAIL ID": "rasiklalbombay@bombayjewels.com"
 },
 {
  "sr.no.": 164,
  "Date": "05-Feb-23",
  "Particulars": "vita trading (krisha)",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 165,
  "Date": "21-Feb-22",
  "Particulars": "Rare Diam",
  "Address": "203, K.L. Accolade,, 6th Road, Near Dena Bank,, Santacruz (East),, Mumbai",
  "GSTIN\/UIN": "27AAXFR3878A1ZO",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 166,
  "Date": "21-Feb-22",
  "Particulars": "Vipul Diamond",
  "Address": "10, 1001, Bhoomi Tower,, Nehru Road,, Santacruz,, Mumbai",
  "GSTIN\/UIN": "27AAAFV5324N1ZV",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 167,
  "Date": "21-Feb-22",
  "Particulars": "Aayushi Impex",
  "Address": "Bw-1050, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAWFA8370R1ZA",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 168,
  "Date": "21-Feb-22",
  "Particulars": "Alok Impex Private Limited",
  "Address": "Plot No. 2 &amp; 3, The Purushottam Ginning Mills Compound, Khand Bazaar, A.K Road,, Surat",
  "GSTIN\/UIN": "24AAACA1033E1ZL",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9925207249,
  "NAME": "Deepak Lalwani",
  "EMAIL ID": "Vinod.soni@kgkmail.com"
 },
 {
  "sr.no.": 169,
  "Date": "23-Feb-22",
  "Particulars": "Shree Siddh Laxmi Diamonds",
  "Address": "4th, 404, Orion Business Park,, Nehru Road,, Santacruz (East),, Mumbai",
  "GSTIN\/UIN": "27AANFS9827L1Z9",
  "QUantity": "1 Unit",
  "CONTACT NO.": 33923223,
  "NAME": "HITESHBHAI J. PATEL",
  "EMAIL ID": "ACCOUNTS@SSLD.IN"
 },
 {
  "sr.no.": 170,
  "Date": "02-Mar-22",
  "Particulars": "Mata Gems LLP",
  "Address": "GW-6070, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East), Mumbai - 400 051",
  "GSTIN\/UIN": "27ABTFM1188P1Z9",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 171,
  "Date": "08-Mar-22",
  "Particulars": "STELLAIRE GEMS PVT. LTD.",
  "Address": "FC-2120, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27ABFCS7628M1ZO",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 172,
  "Date": "10-Mar-22",
  "Particulars": "Sejal Exports (India)",
  "Address": "DC 7221, Bharat Diamond Bourse, Bandra Kurla Complex, Bandra ( East ), Mumbai",
  "GSTIN\/UIN": "27AAAFS7201B1ZR",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9867098700,
  "NAME": "taroon",
  "EMAIL ID": "sejalexport301@hotmail.com"
 },
 {
  "sr.no.": 173,
  "Date": "15-Mar-22",
  "Particulars": "Hasmukhbhai Karamshibhai Kakadiya",
  "Address": "Saurashtra Ind. Soc; Near Savani Road,, Varachha Road,, Surat",
  "GSTIN\/UIN": "24ANNPK9502B1Z8",
  "QUantity": "1 Unit",
  "EMAIL ID": "jagadishkakadiya70@gmail.com"
 },
 {
  "sr.no.": 174,
  "Date": "16-Mar-22",
  "Particulars": "Nidhi Gems",
  "Address": "AE-4042 A, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAAFN2802P1Z6",
  "QUantity": "2 Unit",
  "CONTACT NO.": 9819495088,
  "EMAIL ID": "nidhigems@yahoo.com"
 },
 {
  "sr.no.": 175,
  "Date": "12-Apr-22",
  "Particulars": "AGILE CASTLE INVESTMENTS LLP",
  "Address": "A\/101, Brentwood CHS Ltd., Main Street, Hiranandani Gardens,, Powai, Mumbai",
  "GSTIN\/UIN": "27ABMFA0808P1Z3",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 176,
  "Date": "25-May-22",
  "Particulars": "Nita Exports",
  "Address": "FE-9020, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AABFN5087F1Z7",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9825124184,
  "NAME": "haresh L sonani",
  "EMAIL ID": "nitaexport@yahoo.co.in"
 },
 {
  "sr.no.": 177,
  "Date": "26-May-22",
  "Particulars": "Janki Gems",
  "Address": "BE-1090, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AADFJ0991N1ZX",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9819765056,
  "NAME": "NANJIBHAI LAVJIBHAI PATEL",
  "EMAIL ID": "Janki.gems@yahoo.in"
 },
 {
  "sr.no.": 178,
  "Date": "26-May-22",
  "Particulars": "Samkit Gems",
  "Address": "B-1501, One Avighna Park,, Mahadev Palav Marg,, Curry Road,, Mumbai",
  "GSTIN\/UIN": "27BGKPS8245N1ZG",
  "QUantity": "1 Unit",
  "NAME": "nanji bhai"
 },
 {
  "sr.no.": 179,
  "Date": "01-Jun-22",
  "Particulars": "Rajesh Gems",
  "Address": "JE-5100, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAAFR1413J1ZH",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 180,
  "Date": "20-Jun-22",
  "Particulars": "Sannidhya Diamonds",
  "Address": "DW-3050, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27ACBFS7038P1ZI",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9819169011,
  "NAME": "jagdish bhai",
  "EMAIL ID": "sannidhyadiamonds@gmail.com"
 },
 {
  "sr.no.": 181,
  "Date": "20-Jun-22",
  "Particulars": "Jewels4u",
  "Address": "82\/B Wing, Empire Estate,, Kemps Corner,, August Kranti Marg,, Mumbai",
  "GSTIN\/UIN": "27BHBPP5158H1Z5",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9702616417,
  "NAME": "Pryul vishwas"
 },
 {
  "sr.no.": 182,
  "Date": "23-Jun-22",
  "Particulars": "Shiv-Om Diamonds",
  "Address": "DC-4050, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra(East),, Mumbai",
  "GSTIN\/UIN": "27AABFS7703D1ZF",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9892192130,
  "NAME": "jadhavbhai mohanbhai savani",
  "EMAIL ID": "shivom4050@gmail.com"
 },
 {
  "sr.no.": 183,
  "Date": "04-Jul-22",
  "Particulars": "Jewels by Udit",
  "Address": "Shop No.2, Shopping Arcade Level,, Le Meridian Hotel Windsor Palace,, Central Delhi,",
  "GSTIN\/UIN": "07AYSPG0900D1ZT",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 184,
  "Date": "08-Jul-22",
  "Particulars": "Trezza Jewels LLP",
  "Address": "Unit 007, Tower I, Seepz, Andheri (East),, Mumbai",
  "GSTIN\/UIN": "27AAEFJ1099G1ZA",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820020499,
  "NAME": "Nimith",
  "EMAIL ID": "info@trezzajewles.com"
 },
 {
  "sr.no.": 185,
  "Date": "13-Jul-22",
  "Particulars": "Ramkrishna Diamond Pvt. Ltd.",
  "Address": "5-6, Dongrewadi, Opp. Afil Tower,, Beside Royal Arcade, L.H. Road,, Varachha,, Surat",
  "GSTIN\/UIN": "24AAKCR0209D1ZW",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9924078029,
  "NAME": "Jayu bhai"
 },
 {
  "sr.no.": 186,
  "Date": "19-Jul-22",
  "Particulars": "RK Savani Jewels",
  "Address": "90\/16, Atan Building, Amman Sannathi,, Karaikudi, Sivaganga,, Tamilnadu",
  "GSTIN\/UIN": "33BHNPP8473K2ZK",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 187,
  "Date": "25-Jul-22",
  "Particulars": "Rudra Gems",
  "Address": "107\/108\/109, Kamal Park Society-2,, Near Little Flower School,, Kapodara, Varachha Road,, Surat,",
  "GSTIN\/UIN": "24ABAFR7305L1Z6",
  "QUantity": "1 Unit",
  "CONTACT NO.": 7777900598,
  "NAME": "Mihulbhai"
 },
 {
  "sr.no.": 188,
  "Date": "05-Aug-22",
  "Particulars": "Ratnakala Exports Private Limited",
  "Address": "EC-8010B1, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAECR3763L1ZY",
  "QUantity": "1 Unit",
  "CONTACT NO.": 6593,
  "EMAIL ID": "info@ratnakal.com"
 },
 {
  "sr.no.": 189,
  "Date": "18-Aug-22",
  "Particulars": "MAHENDRA BROTHERS EXPORTS PVT. LTD.",
  "Address": "G - BLOCK, 7TH FLOOR, CE-7011, CE-7012, CE-7013,, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AAFCM0246E1ZT",
  "QUantity": "1 Unit",
  "CONTACT NO.": 8900145642,
  "NAME": "mahindra brother kkaka"
 },
 {
  "sr.no.": 190,
  "Date": "30-Aug-22",
  "Particulars": "KGK DIAMONDS (I) PRIVATE LIMITED",
  "Address": "DE-4011-4016, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27AADCK7579A1ZF",
  "QUantity": "2 Unit",
  "CONTACT NO.": 9619188933,
  "NAME": "piyush"
 },
 {
  "sr.no.": 191,
  "Date": "26-Sep-22",
  "Particulars": "Pranami Gems-Navsari",
  "Address": "Synergy Business Park,, Near Bhuvneshwari Nagar,, Chhapra Road, Chhapra,, Navsari",
  "GSTIN\/UIN": "24AAAFP1746L1Z9",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9119808398,
  "NAME": "tushar bhai"
 },
 {
  "sr.no.": 192,
  "Date": "12-Nov-22",
  "Particulars": "Arina Jewellery",
  "Address": "174 A & 185b SDF VI,, Seepz SEZ,, Andheri (East),, Mumbai-",
  "GSTIN\/UIN": "27ABEFA6649Q1ZQ",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820591982,
  "NAME": "Amit bhai"
 },
 {
  "sr.no.": 193,
  "Date": "14-Nov-22",
  "Particulars": "Arina Jewellery",
  "Address": "174 A & 185b SDF VI,, Seepz SEZ,, Andheri (East),, Mumbai-",
  "GSTIN\/UIN": "27ABEFA6649Q1ZQ",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820591982,
  "NAME": "Amit bhai"
 },
 {
  "sr.no.": 194,
  "Date": "15-Nov-22",
  "Particulars": "Prinay Gems",
  "Address": "1401,Green Ridge Tower 1,, New Link Road, Chikuwadi,, Borivali (West),, Mumbai",
  "GSTIN\/UIN": "27AAZFP9281H1Z9",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 195,
  "Date": "26-Dec-22",
  "Particulars": "Dev Labtech Venture Limited",
  "Address": "D-403, Green Woods,, Andheri Kurla Road, Chakala,, Andheri (East),, Mumbai",
  "GSTIN\/UIN": "27AACCG0736E1ZZ",
  "QUantity": "1 Unit"
 },
 {
  "sr.no.": 196,
  "Date": "21-Feb-23",
  "Particulars": "krisha diam",
  "Address": "hk",
  "QUantity": "3 Unit"
 },
 {
  "sr.no.": 197,
  "Date": "20-Mar-23",
  "Particulars": "shine stone",
  "Address": "GW-4033, Bharat Diamond Bourse,, Bandra Kurla Complex,, Bandra (East),, Mumbai",
  "GSTIN\/UIN": "27ADJFS1341J1ZY",
  "QUantity": "1 Unit",
  "CONTACT NO.": 9820595300,
  "NAME": "hitesh mangukia",
  "EMAIL ID": "account@shinestone.co"
 },
 {
  "sr.no.": 198,
  "Date": "06-Apr-23",
  "Particulars": "c k export",
  "QUantity": "1 Unit",
  "CONTACT NO.": "97128 33000",
  "NAME": "BHAVESHBHAI DETROJA",
  "EMAIL ID": "CKEXPORTS00050@GMAIL.COM"
 },

]
new_sales = []
for sales in master_sales:
    date_formate = datetime.datetime.strptime(sales["Date"], "%d-%b-%y").date()
    sales["Date"] = f"{date_formate.day}-{date_formate.month}-{date_formate.year}"
    try:
        sales["GSTIN\\/UIN"] = sales["GSTIN\\/UIN"]
    except KeyError:
        sales["GSTIN\\/UIN"] = None
    try:
        sales["CONTACT NO."] = sales["CONTACT NO."]
    except KeyError:
        sales["CONTACT NO."] = None
    try:
        sales["NAME"] = sales["NAME"]
    except KeyError:
        sales["NAME"] = None
    try:
        sales["EMAIL ID"] = sales["EMAIL ID"]
    except KeyError:
        sales["EMAIL ID"] = None
    try:
        sales["Address"] = sales["Address"]
    except KeyError:
        sales["Address"] = None
    new_sales.append(sales)


with open("new_mastersales.json", "w") as file:
    json.dump(new_sales, fp=file)
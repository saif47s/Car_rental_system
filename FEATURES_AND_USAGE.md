# 🚗 HK Gari Rental Manager - Complete A to Z Guide

Yeh document is software ke baare mein mukammal tafseelat (A to Z) faraham karta hai. Ismein har feature ki wazahat aur usko istemal karne ka tareeqa bataya gaya hai.

---

## 📌 Software Kya Hai? (What is this app?)
Yeh ek **100% Offline Windows Desktop Application** hai jo rent-a-car business ko manage karne ke liye banayi gayi hai. Is software ke zariye aap apni gaariyon ka record, customers ki details, unke baqaya jaat (pending balance), aur daily basis par hone wale kharchon (expenses) ko aasani se track kar sakte hain. 

**Khas Baat:** Ismein kisi internet connection, online server, ya XAMPP jaise complex database setup ki zaroorat nahi hai. Saara data aapke apne computer ki hard drive mein mehfooz hota hai.

---

## 🛠️ Main Features (Khusoosiyat)

### 1. 🏠 Dashboard (Home Screen)
- **Mukhtasar Report:** Is mahine ki total amdani, munafa, aur aaj rent par gayi hui gaariyon ki tadad dikhata hai.
- **Pending Balance:** Jin customers ki taraf paise baqi hain, unki list prominently nazar aati hai taake unse recovery ki ja sakay.
- **Aaj ki Activity:** Aaj ke din kaunsi gari kis customer ke paas gayi hai, uski live detail.

### 2. 📋 Rental Log (Bookings)
- **Naya Rental:** Gari rent par dene ka record enter karna (Gari, Customer, Tarikh, Waqt, Meter Reading, Advance aur Final Rent).
- **Auto Calculations:** Agar gari ka daily rent fix hai toh system khud total calculate kar leta hai. Discount percentage (%) ya exact Amount mein lagaya ja sakta hai.
- **Digital Receipt:** Har rental ki ek digital raseed (receipt) banti hai jise print kiya ja sakta hai.
- **WhatsApp Integration:** App se directly "WhatsApp Pe Bhejein" button click karne se raseed customer ko WhatsApp par chali jati hai.
- **Filters:** Kisi makhsoos mahine ya gari ke hisaab se rental history check ki ja sakti hai.

### 3. 👥 Customers Management
- Naye customers ka record (Naam, Walid ka naam, CNIC, aur Mobile number) mehfooz karna.
- Ek customer ne ab tak kitne trips kiye hain aur uski taraf kitna balance baqi hai, sab ek jagah nazar aata hai.

### 4. 🚗 Vehicles (Gaariyan)
- Apni fleet (gaariyon) ko system mein add karna (Gari No., Model, Saal, Colour aur Fix Rent/Din).
- Har gari ki karkardagi dekhna ke usne ab tak kitne din duty ki hai aur total kitne paise kamaye hain.

### 5. 💸 Kharcha (Expenses)
- Gari ki maintenance (Oil change, tires, workshop) ya office ke rozmarra kharchon (Roz ka kharcha, bills, etc.) ko record karna.
- Yeh kharcha direct aapke net munafa (profit) se minus ho jata hai.

### 6. 📊 Munafa / Nuqsan (Reports)
- **Saalana Report:** Poore saal ki amdani, kharcha aur net munafa ek jhalak mein dekhna.
- **Mahina Wari Chart:** Har mahine ka graph banta hai jisse pata chalta hai ke kis mahine mein sab se zyada profit ya loss hua.

### 7. 💾 Backup & Restore
- **Backup Lein:** App mein "Backup Lein" ka button hai jo aapke saare data ko ek secure `.json` file mein download kar deta hai. Is file ko aap USB ya Email par save kar sakte hain.
- **Restore Karein:** Agar aap naya computer lete hain ya Windows dobara karte hain, toh wohi `.json` file upload kar ke saara data wapis laya ja sakta hai.
- **Excel Export:** Aap apne saare record (Rentals, Customers, Vehicles) ko ek click mein Excel (.csv) file mein download kar sakte hain.

### 8. 🗑️ Recycle Bin (Trash)
- Agar koi record ghalti se delete ho jaye toh woh foran zaya nahi hota. Woh Recycle Bin mein chala jata hai.
- Aap wahan se data ko Restore (wapis lana) ya Permanent Delete kar sakte hain.

---

## 💻 App Kaise Istemal Karein? (How to Use?)

1. **Software Open Karein:** Apne Desktop par maujood `HK Gari Rental Manager` icon par double-click karein.
2. **Pehla Kaam (Add Vehicles):** Sab se pehle `Vehicles` tab mein ja kar apni saari gaariyan add karein aur unka daily rent tay karein.
3. **Doosra Kaam (Add Customers):** Uske baad `Customers` tab mein regular customers ka data add karein. (Aap Rental enter karte waqt bhi naya customer add kar sakte hain).
4. **Gari Rent Par Dena:** Jab bhi gari rent par deni ho, `Rental Log` mein jayen -> `Naya Rental Darj Karein` par click karein. Gari select karein, customer select karein, advance amount likhein aur Save kar dein.
5. **Raseed Bhejna:** Save hone ke baad usi record ke aage `🧾` icon par click karein aur WhatsApp ke zariye raseed customer ko bhej dein.
6. **Rozana ka Check:** Jab bhi gari wapis aaye, us rental ko Edit (`✏️`) karein aur 'Aaya' waqt aur Meter IN (KM) update karein.

---
**Tech Stack Used:** 
- HTML5, CSS3 (Custom UI without external frameworks)
- Vanilla JavaScript (Local Storage for Database)
- Electron.js & Node.js (For Windows Executable Packaging)

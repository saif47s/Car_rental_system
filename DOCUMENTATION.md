# HK Gari Rental Management System - Mukammal Tafseelat (A to Z)

Yeh aik aisi application hai jo rent-a-car business ko digital aur asan banati hai. Yeh offline chalti hai, aur is mein customer ka record, gariyan, bookings, kharcha, aur munafa asani se manage kiya ja sakta hai.

## 1. Setup aur Login 🔐
- **Pin Setup**: Jab pehli dafa software chalta hai to 4-digit PIN set karna padta hai.
- **Login**: Us PIN aur username ko use kar ke software login hota hai. Agar password bhool jayen, to "Forgot Password" option istemal kar sakte hain jahan security question pucha jayega (jaise "Is fleet company ka naam kya hai?").
- **Security Question**: Settings mein ja kar apna security sawal aur jawab set kiya ja sakta hai jo baad mein password reset karne ke kaam aayega.

## 2. Dashboard 📊
- **Stats Overview**: Total Gaariyan, Total Kharcha, Munafa (Profit), aur total pending items yahan asani se nazar aate hain.
- **Summary Box**: Ye section quick overview deta hai takay app kholte hi business ki position pata chal jaye.

## 3. Rental Log 📝
- **Rent Entry**: "Naya Rental Darj Karein" pe click kar ke gari, customer, dates, aur kiraya likh sakte hain.
- **Pending/Completed Filter**: Sirf pending (jin ka balance baqi ho) rentals filter kar sakte hain ya specific date se log filter kar sakte hain.
- **WhatsApp**: Rental receipt ka detail WhatsApp ke zariye aik click se direct customer ko send kar sakte hain.
- **Excel Export**: Tamam records 1 click se Excel sheet mein download ho sakte hain.

## 4. Booking Log 🗓️
- **Advance Booking**: Kisi customer ne agar gari aglay haftay ke liye book ki hai, to yahan record darj kiya jata hai.
- **Advance Payment**: Booking ke waqt advance payment ka record rakha ja sakta hai.
- Is tab mein bhi WhatsApp sharing aur Excel export majood hai.

## 5. Customers 👤
- **Customer Record**: Naya customer add karein (Naam, CNIC, Mobile No. waghera).
- **Edit/Delete**: Kisi bhi waqt in details ko update ya remove kiya ja sakta hai.
- Iska database Rental aur Booking logs se linked hai. Jab naya rent banayenge, to customer ka naam dropdown list mein khud ba khud aa jayega.

## 6. Vehicles (Gariyan) 🚗
- **Gaari Add Karein**: Apni company ki nayi gariyan add kar sakte hain. Model, number plate, aur daily rent specify kiya ja sakta hai.
- **Commission/Owner**: Agar gari apni na ho, balki kisi teesre party ki ho, to owner aur commission ka profit hisaab rakha ja sakta hai.

## 7. Kharcha (Expenses) 💸
- **Roozana Ke Kharchay**: Petrol, maintenance, car wash, aur staff salary waghera ki details is tab mein dali jati hain.
- Yeh tamam entries mahana (monthly) aur salana (yearly) munafa/nuqsan report mein calculate hoti hain.

## 8. Munafa / Nuqsan (Profit & Loss) 📈
- **Graphical Report**: Saal (Year) select kar ke har maheene ka hisaab dekhein.
- **Amdani vs Kharcha**: Poore saal mein kitna kiraya aya aur kitna kharcha hua, dono minus ho kar exact munafa (Profit) bataya jata hai. Bar charts color coding ke sath show hotay hain (Sabz matlab Profit, Laal matlab Loss).

## 9. Backup / Restore 💾
- **Data Safe**: Choonke yeh app offline hai, is liye apna data mahfooz rakhne ke liye "Download Backup" button istemal karein. Yeh saara data JSON file ki shakal mein save kar lega.
- **Restore Data**: Agar computer tabdeel karna ho ya data dobara wapis lana ho, to "Restore Backup" se wahi file select karein aur sara record 1 second mein wapis aa jayega.

## 10. Recycle Bin 🗑️
- **Ghalati se Delete Shuda Data**: Agar koi Rental, Booking ya Customer ghalati se delete ho jaye, to woh foran hamesha ke liye khatam nahi hota. Woh Recycle Bin mein chala jata hai jahan se "Restore" button click kar ke usay wapis laya ja sakta hai.

## 11. Reset PIN ⚙️
- Agar apna mojooda 4 digit login PIN change karna ho, to yahan purana PIN daal kar naya PIN rakha ja sakta hai.

## Troubleshooting Error (Win 7/8 Installation) ⚠️
- Pehle jo `.lnk` error (Unspecified error) aarha tha uski wajah Windows 7 mein Start Menu shortcut ban-ne ka masla tha.
- **Solution**: Nayi `v5.0` update mein Electron ka version downgrade kiya gaya hai aur shortcut generation system modify kar diya gaya hai. Ab aap naya Setup chalayen to Windows 7 ya 32-bit systems mein bhi easily install ho jayega.

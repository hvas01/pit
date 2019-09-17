# (Vietnam) Monthly Personal Income Tax

Công cụ tính thuế thu nhập cá nhân (tạm đóng), bảo hiểm bắt buộc (BHXH, BHYT, BHTN), tiền lương net hàng tháng.

(Áp dụng tỉ lệ đóng bảo hiểm, thuế thu nhập cá nhân trong 2019, mức lương cơ sở, lương tối thiểu theo vùng từ 01/07/2019)

1. Nhập thông tin thu nhập hàng tháng
   
![](https://i.imgur.com/pGHDDU8.png)

2. Vùng kết quả 
   
![](https://i.imgur.com/IQchPAC.png)

3. Triển khai lên Google App Engine

- Trên Google Cloud, tạo Project mới (lấy thông tin PROJECT_ID)
- Trên máy dev, clone github repo về.
- Mở Google Cloud SDK Shell, chuyển về thư mục repo 'pit'
- Thực hiện deploy lên Google App Engine

```
gcloud auth application-default login
gcloud config set project PROJECT_ID
gcloud app deploy app.yaml
```
Lựa chọn các tùy chọn triển khai App Engine theo chỉ dẫn trên màn hình.

Demo app: https://hva-app-pit.appspot.com/

### Thông tin thêm:
Thông tin tỉ lệ đóng BHXH, BHYT, BHTN (2019)
- BHXH: 8% (không quá 20 lần mức lương cơ sở).
- BHYT: 1.5% (không quá 20 lần mức lương cơ sở).
- BHTN: 1% (không quá 20 lần mức lương tối thiểu vùng).

Lương cơ sở: 1.490.000 đồng/tháng (từ 01/07/2019)

Lương tối thiếu theo vùng:
- Vùng I: 4.180.000 đồng/tháng (Hà Nội, Quảng Ninh, Đà Nẵng, Tp.HCM, Bình Dương, Đồng Nai, Vũng Tàu.)
- Vùng II: 3.710.000 đồng/tháng (Hải Phòng, Vĩnh Phúc, Thái Nguyên, Khánh Hoà, Bình Phước, Tây Ninh, Long An, An Giang, Cần Thơ, Cà Mau.)
- Vùng III: 3.250.000 đồng/tháng (Hà Tây, Bắc Ninh, Hải Dương, Hưng Yên, Huế, Bình Định, Gia Lai, Đắc Lắc, Lâm Đồng, Ninh Thuận, Bình Thuận, ĐồngTháp, Tiền Giang, Vĩnh Long, Bến Tre, Kiên Giang, Hậu Giang, Sóc Trăng, Bạc Liêu.)
- Vùng IV: 2.920.000 đồng/tháng (là các tỉnh còn lại.)

Bảng mức thuế thu nhập cá nhân

Trong bảng bên dưới, chữ viết tắt TN là số tiền thu nhập chịu thuế theo tháng (sau khi đã trừ đi các khoản bảo hiểm và giảm trừ gia cảnh).

Bậc | Thu nhập tháng | Số thuế phải nộp
--- | -------------- | ----------------
1 | TN <= 5tr | TN x 5%
2 | 5tr < TN <= 10tr | TN x 10% - 0.25tr
3 | 10tr < TN <= 18tr | TN x 15% - 0.75tr
4 | 18tr < TN <= 32tr | TN x 20% - 1.65tr
5 | 32tr < TN <= 52tr | TN x 25% - 3.25tr
6 | 52tr < TN <= 80tr | TN x 30% - 5.85tr
7 | TN > 80tr | TN x 35% - 9.85tr
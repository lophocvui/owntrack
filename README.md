# owntrack and python
Owntrack iot platform
Việc giả lập một đối tượng đang di chuyển trong bản đồ tương đối đơn giản. Ta chỉ cần một ngôn ngữ lập trình có hỗ trợ thư viện mqtt là hoàn toàn có thể làm được việc này. Bản chât của việc lập trình là sử dụng các hàm sẵn có trong thư viện để gửi các tin nhắn đến MQTT Broker. Các tin nhắn chứa các thông tin đầy đủ của thiết bị như vị trí tọa độ, mức PIN còn lại hay trạng thái hoạt động. Với sự thay đôỉ ngẫu nhiên của tọa độ và thời gian thực kèm theo, ta có được hình ảnh trực quan về một thiết bị giống như đang di chuyển được hiển thị trên bản đồ. Ta cũng có thể tính toán được tốc độ di chuyển của các thiết bị bằng một số công thức toán học thông qua thư viện math tương ứng với từng ngôn ngữ lập trình.
Và tôi dùng python trong ví dụ của mình

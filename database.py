from motor.motor_asyncio import AsyncIOMotorClient

	# رابط اتصال MongoDB (قم بتعديله حسب الإعدادات الخاصة بك)
MONGO_URI = "mongodb://localhost:27017"  # أو رابط Atlas MongoDB

	# إنشاء عميل MongoDB
client = AsyncIOMotorClient(MONGO_URI)

	# اختيار قاعدة البيانات
db = client["mydatabase"]  # قم بتغيير اسم قاعدة البيانات
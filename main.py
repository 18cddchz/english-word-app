from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.storage.jsonstore import JsonStore
from kivy.core.text import LabelBase
from kivy.graphics import Color, Rectangle
import json
import random
import os

# ===================== 界面配色（米黄护眼）=====================
BG_COLOR = [1, 0.97, 0.86, 1]
TEXT_COLOR = [0, 0, 0, 1]
RIGHT_COLOR = [0, 0.7, 0, 1]
WRONG_COLOR = [0.8, 0, 0, 1]
# 字号放大一倍
FONT_SIZE_NORMAL = 48
FONT_SIZE_BIG = 48

# ========== 注册中文字体 DroidSansFallback.ttf 同目录 ==========
try:
    # 字体文件和main.py放同一文件夹
    LabelBase.register(name="DroidSans", fn_regular="DroidSansFallback.ttf")
    FONT_NAME = "DroidSans"
except Exception as e:
    # 找不到字体就用系统默认兜底，防止崩溃
    print("字体加载失败，使用默认字体", e)
    FONT_NAME = None

# ===================== 人教PEP 3~6年级 单词+句子+短文 完整库 =====================
word_data = {
    "3年级上册": {
        "words": [
            {"en":"ruler", "cn":"尺子"},
            {"en":"pencil", "cn":"铅笔"},
            {"en":"eraser", "cn":"橡皮"},
            {"en":"crayon", "cn":"蜡笔"},
            {"en":"bag", "cn":"包"},
            {"en":"pen", "cn":"钢笔"},
            {"en":"pencil box", "cn":"铅笔盒"},
            {"en":"book", "cn":"书"},
            {"en":"red", "cn":"红色"},
            {"en":"yellow", "cn":"黄色"},
            {"en":"green", "cn":"绿色"},
            {"en":"blue", "cn":"蓝色"},
            {"en":"black", "cn":"黑色"},
            {"en":"brown", "cn":"棕色"},
            {"en":"white", "cn":"白色"},
            {"en":"orange", "cn":"橙色"},
            {"en":"cat", "cn":"猫"},
            {"en":"dog", "cn":"狗"},
            {"en":"monkey", "cn":"猴子"},
            {"en":"bird", "cn":"鸟"}
        ],
        "sentences": [
            {"en":"Hello! I'm Wu Yifan.", "cn":"你好！我是吴一凡。"},
            {"en":"Good morning.", "cn":"早上好。"},
            {"en":"Nice to meet you.", "cn":"很高兴见到你。"},
            {"en":"What's your name? My name's John.", "cn":"你叫什么名字？我叫约翰。"},
            {"en":"How are you? I'm fine, thank you.", "cn":"你好吗？我很好，谢谢你。"}
        ],
        "articles": [
            {"en":"Hello, my name is Amy.\nI have a new bag.\nIt is blue.\nI like my bag.",
             "cn":"你好，我叫艾米。\n我有一个新书包。\n它是蓝色的。\n我喜欢我的书包。"}
        ]
    },
    "3年级下册": {
        "words": [
            {"en":"UK", "cn":"英国"},
            {"en":"Canada", "cn":"加拿大"},
            {"en":"USA", "cn":"美国"},
            {"en":"China", "cn":"中国"},
            {"en":"she", "cn":"她"},
            {"en":"student", "cn":"学生"},
            {"en":"pupil", "cn":"小学生"},
            {"en":"teacher", "cn":"教师"},
            {"en":"he", "cn":"他"},
            {"en":"boy", "cn":"男孩"},
            {"en":"girl", "cn":"女孩"},
            {"en":"father", "cn":"父亲"},
            {"en":"dad", "cn":"爸爸"},
            {"en":"mother", "cn":"母亲"},
            {"en":"mum", "cn":"妈妈"},
            {"en":"sister", "cn":"姐妹"},
            {"en":"brother", "cn":"兄弟"},
            {"en":"thin", "cn":"瘦的"},
            {"en":"fat", "cn":"胖的"},
            {"en":"tall", "cn":"高的"}
        ],
        "sentences": [
            {"en":"Where are you from? I'm from China.", "cn":"你来自哪里？我来自中国。"},
            {"en":"This is my family.", "cn":"这是我的家庭。"},
            {"en":"Who's that man? He's my father.", "cn":"那个男人是谁？他是我的爸爸。"},
            {"en":"It has a long nose.", "cn":"它有长鼻子。"},
            {"en":"Do you like oranges? Yes, I do.", "cn":"你喜欢橙子吗？是的，我喜欢。"}
        ],
        "articles": [
            {"en":"I have a family.\nMy dad is tall.\nMy mum is nice.\nI love my family.",
             "cn":"我有一个家庭。\n我的爸爸很高。\n我的妈妈很和善。\n我爱我的家人。"}
        ]
    },
    "4年级上册": {
        "words": [
            {"en":"classroom", "cn":"教室"},
            {"en":"window", "cn":"窗户"},
            {"en":"blackboard", "cn":"黑板"},
            {"en":"light", "cn":"电灯"},
            {"en":"picture", "cn":"图画"},
            {"en":"door", "cn":"门"},
            {"en":"computer", "cn":"电脑"},
            {"en":"fan", "cn":"风扇"},
            {"en":"wall", "cn":"墙壁"},
            {"en":"floor", "cn":"地板"},
            {"en":"schoolbag", "cn":"书包"},
            {"en":"Chinese book", "cn":"语文书"},
            {"en":"English book", "cn":"英语书"},
            {"en":"maths book", "cn":"数学书"},
            {"en":"storybook", "cn":"故事书"},
            {"en":"candy", "cn":"糖果"},
            {"en":"toy", "cn":"玩具"},
            {"en":"key", "cn":"钥匙"},
            {"en":"strong", "cn":"强壮的"},
            {"en":"friendly", "cn":"友好的"}
        ],
        "sentences": [
            {"en":"Let's clean the classroom.", "cn":"让我们打扫教室。"},
            {"en":"What's in your schoolbag?", "cn":"你的书包里面有什么？"},
            {"en":"He has glasses and his shoes are blue.", "cn":"他戴眼镜，鞋子是蓝色的。"},
            {"en":"What would you like for dinner?", "cn":"晚餐你想吃什么？"},
            {"en":"I'd like some rice and soup.", "cn":"我想要一些米饭和汤。"}
        ],
        "articles": [
            {"en":"Our classroom is big.\nWe have a blackboard.\nWe read books here.\nWe love our classroom.",
             "cn":"我们的教室很大。\n我们有一块黑板。\n我们在这里读书。\n我们爱我们的教室。"}
        ]
    },
    "4年级下册": {
        "words": [
            {"en":"first floor", "cn":"一楼"},
            {"en":"second floor", "cn":"二楼"},
            {"en":"library", "cn":"图书馆"},
            {"en":"playground", "cn":"操场"},
            {"en":"garden", "cn":"花园"},
            {"en":"teacher's office", "cn":"教师办公室"},
            {"en":"breakfast", "cn":"早餐"},
            {"en":"lunch", "cn":"午餐"},
            {"en":"dinner", "cn":"晚餐"},
            {"en":"get up", "cn":"起床"},
            {"en":"go to school", "cn":"去上学"},
            {"en":"go home", "cn":"回家"},
            {"en":"go to bed", "cn":"上床睡觉"},
            {"en":"cold", "cn":"寒冷的"},
            {"en":"hot", "cn":"热的"},
            {"en":"warm", "cn":"温暖的"},
            {"en":"cool", "cn":"凉爽的"},
            {"en":"sunny", "cn":"晴朗的"},
            {"en":"windy", "cn":"有风的"},
            {"en":"cloudy", "cn":"多云的"}
        ],
        "sentences": [
            {"en":"Where is the library? It's on the second floor.", "cn":"图书馆在哪里？它在二楼。"},
            {"en":"What time is it? It's nine o'clock.", "cn":"几点了？九点了。"},
            {"en":"It's time for English class.", "cn":"该上英语课了。"},
            {"en":"What's the weather like today?", "cn":"今天天气怎么样？"},
            {"en":"It's sunny in Beijing.", "cn":"北京天气晴朗。"}
        ],
        "articles": [
            {"en":"I get up at seven.\nI go to school at eight.\nI have lunch at twelve.\nI go to bed at nine.",
             "cn":"我七点起床。\n我八点去上学。\n我十二点吃午饭。\n我九点上床睡觉。"}
        ]
    },
    "5年级上册": {
        "words": [
            {"en":"old", "cn":"老的；年纪大的"},
            {"en":"young", "cn":"年轻的"},
            {"en":"funny", "cn":"滑稽的"},
            {"en":"kind", "cn":"和蔼的"},
            {"en":"strict", "cn":"严厉的"},
            {"en":"polite", "cn":"有礼貌的"},
            {"en":"hard-working", "cn":"勤奋的"},
            {"en":"helpful", "cn":"乐于助人的"},
            {"en":"shy", "cn":"害羞的"},
            {"en":"clever", "cn":"聪明的"},
            {"en":"Monday", "cn":"星期一"},
            {"en":"Tuesday", "cn":"星期二"},
            {"en":"Wednesday", "cn":"星期三"},
            {"en":"Thursday", "cn":"星期四"},
            {"en":"Friday", "cn":"星期五"},
            {"en":"Saturday", "cn":"星期六"},
            {"en":"Sunday", "cn":"星期日"},
            {"en":"wash", "cn":"洗"},
            {"en":"watch", "cn":"看"},
            {"en":"read", "cn":"读"}
        ],
        "sentences": [
            {"en":"What's he like? He is young and kind.", "cn":"他是什么样的人？他年轻又和蔼。"},
            {"en":"What do you have on Mondays?", "cn":"星期一你有什么课？"},
            {"en":"I have Chinese and English.", "cn":"我有语文课和英语课。"},
            {"en":"What do you often do on the weekend?", "cn":"周末你经常做什么？"},
            {"en":"I often read books on Saturday.", "cn":"我经常在周六看书。"}
        ],
        "articles": [
            {"en":"My English teacher is Ms Wang.\nShe is kind and funny.\nI like English class.\nI read books on weekends.",
             "cn":"我的英语老师是王老师。\n她和蔼又有趣。\n我喜欢英语课。\n我周末看书。"}
        ]
    },
    "5年级下册": {
        "words": [
            {"en":"eat breakfast", "cn":"吃早饭"},
            {"en":"have class", "cn":"上课"},
            {"en":"play sports", "cn":"进行体育运动"},
            {"en":"do morning exercises", "cn":"做早操"},
            {"en":"eat dinner", "cn":"吃晚饭"},
            {"en":"take a dancing class", "cn":"上舞蹈课"},
            {"en":"spring", "cn":"春天"},
            {"en":"summer", "cn":"夏天"},
            {"en":"autumn", "cn":"秋天"},
            {"en":"winter", "cn":"冬天"},
            {"en":"season", "cn":"季节"},
            {"en":"pick apples", "cn":"摘苹果"},
            {"en":"go swimming", "cn":"去游泳"},
            {"en":"go skating", "cn":"去滑冰"},
            {"en":"January", "cn":"一月"},
            {"en":"February", "cn":"二月"},
            {"en":"March", "cn":"三月"},
            {"en":"April", "cn":"四月"},
            {"en":"May", "cn":"五月"},
            {"en":"June", "cn":"六月"}
        ],
        "sentences": [
            {"en":"When do you get up? I get up at 7 o'clock.", "cn":"你什么时候起床？我七点起床。"},
            {"en":"Which season do you like best?", "cn":"你最喜欢哪个季节？"},
            {"en":"I like summer best. I can swim.", "cn":"我最喜欢夏天。我可以游泳。"},
            {"en":"When is the party? It's in April.", "cn":"派对在什么时候？在四月。"},
            {"en":"My birthday is on June 1st.", "cn":"我的生日在6月1日。"}
        ],
        "articles": [
            {"en":"I like spring best.\nThe trees turn green.\nI can fly kites.\nSpring is beautiful.",
             "cn":"我最喜欢春天。\n树木变绿。\n我可以放风筝。\n春天很美。"}
        ]
    },
    "6年级上册": {
        "words": [
            {"en":"science", "cn":"科学"},
            {"en":"museum", "cn":"博物馆"},
            {"en":"post office", "cn":"邮局"},
            {"en":"bookstore", "cn":"书店"},
            {"en":"cinema", "cn":"电影院"},
            {"en":"hospital", "cn":"医院"},
            {"en":"crossing", "cn":"十字路口"},
            {"en":"turn left", "cn":"左转"},
            {"en":"turn right", "cn":"右转"},
            {"en":"go straight", "cn":"直走"},
            {"en":"subway", "cn":"地铁"},
            {"en":"train", "cn":"火车"},
            {"en":"plane", "cn":"飞机"},
            {"en":"ship", "cn":"轮船"},
            {"en":"slow", "cn":"慢的"},
            {"en":"stop", "cn":"停下"},
            {"en":"visit", "cn":"拜访"},
            {"en":"film", "cn":"电影"},
            {"en":"trip", "cn":"旅行"},
            {"en":"supermarket", "cn":"超市"}
        ],
        "sentences": [
            {"en":"Where is the museum shop?", "cn":"博物馆商店在哪里？"},
            {"en":"It's near the door.", "cn":"它在门旁边。"},
            {"en":"How can I get there? Turn right at the hospital.", "cn":"我怎么到那里？在医院右转。"},
            {"en":"How do you go to school? By bus.", "cn":"你怎么去上学？坐公交车。"},
            {"en":"What are you going to do tomorrow?", "cn":"你明天打算做什么？"}
        ],
        "articles": [
            {"en":"I want to go to the bookstore.\nIt's next to the hospital.\nI will buy a storybook.\nI will go by bus.",
             "cn":"我想去书店。\n书店在医院旁边。\n我要买一本故事书。\n我坐公交车过去。"}
        ]
    },
    "6年级下册": {
        "words": [
            {"en":"younger", "cn":"更年轻的"},
            {"en":"older", "cn":"更年长的"},
            {"en":"taller", "cn":"更高的"},
            {"en":"shorter", "cn":"更矮的；更短的"},
            {"en":"longer", "cn":"更长的"},
            {"en":"thinner", "cn":"更瘦的"},
            {"en":"heavier", "cn":"更重的"},
            {"en":"bigger", "cn":"更大的"},
            {"en":"smaller", "cn":"更小的"},
            {"en":"stronger", "cn":"更强壮的"},
            {"en":"dinosaur", "cn":"恐龙"},
            {"en":"hall", "cn":"大厅"},
            {"en":"metre", "cn":"米"},
            {"en":"kilogram", "cn":"千克"},
            {"en":"cleaned", "cn":"打扫"},
            {"en":"washed", "cn":"洗"},
            {"en":"watched", "cn":"看"},
            {"en":"stayed", "cn":"停留"},
            {"en":"read", "cn":"读"},
            {"en":"had", "cn":"有；吃"}
        ],
        "sentences": [
            {"en":"How tall are you? I'm 1.6 metres.", "cn":"你多高？我1.6米。"},
            {"en":"You are taller than me.", "cn":"你比我高。"},
            {"en":"What did you do last weekend?", "cn":"上周末你做了什么？"},
            {"en":"I watched TV at home.", "cn":"我在家看电视。"},
            {"en":"Did you go to the park? Yes, I did.", "cn":"你去公园了吗？是的。"}
        ],
        "articles": [
            {"en":"Last weekend I stayed at home.\nI cleaned my room.\nI read a storybook.\nI had a happy weekend.",
             "cn":"上周末我待在家里。\n我打扫了房间。\n我读了一本故事书。\n我度过了愉快的周末。"}
        ]
    }
}

# 本地数据存储（错题、收藏、统计）
store = JsonStore("english_data.json")

# 屏幕管理器
sm = ScreenManager()

# 主界面
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        # 修复背景：用Color+Rectangle替代旧的错误写法
        with layout.canvas.before:
            Color(*BG_COLOR)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        def update_rect(instance, value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size
        layout.bind(pos=update_rect, size=update_rect)
        self.add_widget(layout)

        title_label = Label(text="程君瑞同学英语学习", font_name=FONT_NAME, font_size=FONT_SIZE_BIG, color=TEXT_COLOR, size_hint_y=0.12)
        layout.add_widget(title_label)

        grade_layout = GridLayout(cols=4, size_hint_y=0.15, spacing=10)
        self.grade_btn_dict = {}
        for grade in ["3年级上册","3年级下册","4年级上册","4年级下册","5年级上册","5年级下册","6年级上册","6年级下册"]:
            btn = Button(text=grade, font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL, background_color=[0.2,0.6,0.8,1])
            btn.bind(on_press=self.select_grade)
            self.grade_btn_dict[btn] = grade
            grade_layout.add_widget(btn)
        layout.add_widget(grade_layout)

        mode_layout = GridLayout(cols=2, size_hint_y=0.15, spacing=10)
        btn_word = Button(text="单词练习", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL)
        btn_sentence = Button(text="句子短文", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL)
        btn_word.bind(on_press=self.goto_word)
        btn_sentence.bind(on_press=self.goto_sentence)
        mode_layout.add_widget(btn_word)
        mode_layout.add_widget(btn_sentence)
        layout.add_widget(mode_layout)

        func_layout = GridLayout(cols=3, size_hint_y=0.15, spacing=10)
        btn_fav = Button(text="收藏单词", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL)
        btn_wrong = Button(text="错题本", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL)
        btn_stat = Button(text="学习统计", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL)
        btn_fav.bind(on_press=self.goto_fav)
        btn_wrong.bind(on_press=self.goto_wrong)
        btn_stat.bind(on_press=self.goto_stat)
        func_layout.add_widget(btn_fav)
        func_layout.add_widget(btn_wrong)
        func_layout.add_widget(btn_stat)
        layout.add_widget(func_layout)
        self.selected_grade = None

    def select_grade(self, instance):
        self.selected_grade = self.grade_btn_dict[instance]
        instance.background_color = [0,0.7,0,1]

    def goto_word(self, instance):
        if not self.selected_grade:
            return
        word_screen = sm.get_screen("word")
        word_screen.load_grade(self.selected_grade, "word")
        sm.current = "word"

    def goto_sentence(self, instance):
        if not self.selected_grade:
            return
        sentence_screen = sm.get_screen("word")
        sentence_screen.load_grade(self.selected_grade, "sentence")
        sm.current = "word"

    def goto_fav(self, instance):
        fav_screen = sm.get_screen("fav")
        fav_screen.load_data()
        sm.current = "fav"

    def goto_wrong(self, instance):
        wrong_screen = sm.get_screen("wrong")
        wrong_screen.load_data()
        sm.current = "wrong"

    def goto_stat(self, instance):
        stat_screen = sm.get_screen("stat")
        stat_screen.load_stat()
        sm.current = "stat"

# 练习页面（单词/句子/短文共用）
class WordScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.item_list = []
        self.current_item = None
        self.item_type = "word"
        self.grade = ""
        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)
        # 修复背景
        with layout.canvas.before:
            Color(*BG_COLOR)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        def update_rect(instance, value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size
        layout.bind(pos=update_rect, size=update_rect)
        self.add_widget(layout)

        self.question_label = Label(text="请选择年级后开始练习", font_name=FONT_NAME, font_size=FONT_SIZE_BIG, color=TEXT_COLOR, size_hint_y=0.2)
        layout.add_widget(self.question_label)

        self.answer_input = TextInput(hint_text="在这里输入答案", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL, size_hint_y=0.15, multiline=True)
        layout.add_widget(self.answer_input)

        self.result_label = Label(text="", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL, size_hint_y=0.15)
        layout.add_widget(self.result_label)

        btn_layout = GridLayout(cols=3, size_hint_y=0.12, spacing=8)
        btn_read = Button(text="🔊朗读", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL)
        btn_submit = Button(text="✅提交答案", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL)
        btn_next = Button(text="➡下一题", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL)
        btn_read.bind(on_press=self.read_aloud)
        btn_submit.bind(on_press=self.check_answer)
        btn_next.bind(on_press=self.next_item)
        btn_layout.add_widget(btn_read)
        btn_layout.add_widget(btn_submit)
        btn_layout.add_widget(btn_next)
        layout.add_widget(btn_layout)

        btn_layout2 = GridLayout(cols=3, size_hint_y=0.12, spacing=8)
        btn_trans_e2c = Button(text="英译汉", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL)
        btn_trans_c2e = Button(text="汉译英", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL)
        btn_fav = Button(text="⭐收藏", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL)
        btn_trans_e2c.bind(on_press=lambda x:self.set_mode("e2c"))
        btn_trans_c2e.bind(on_press=lambda x:self.set_mode("c2e"))
        btn_fav.bind(on_press=self.add_fav)
        btn_layout2.add_widget(btn_trans_e2c)
        btn_layout2.add_widget(btn_trans_c2e)
        btn_layout2.add_widget(btn_fav)
        layout.add_widget(btn_layout2)

        btn_back = Button(text="返回主页", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL, size_hint_y=0.08)
        btn_back.bind(on_press=lambda x: setattr(sm, "current", "main"))
        layout.add_widget(btn_back)
        self.mode = "e2c"

    def load_grade(self, grade, item_type):
        self.grade = grade
        self.item_type = item_type
        if item_type == "word":
            self.item_list = word_data[grade]["words"]
        elif item_type == "sentence":
            self.item_list = word_data[grade]["sentences"] + word_data[grade]["articles"]
        random.shuffle(self.item_list)
        self.next_item(None)

    def set_mode(self, mode):
        self.mode = mode
        self.next_item(None)

    def next_item(self, instance):
        if len(self.item_list) <= 0:
            self.question_label.text = "本年级练习完成！"
            self.result_label.text = ""
            return
        self.current_item = random.choice(self.item_list)
        self.answer_input.text = ""
        self.result_label.text = ""
        if self.mode == "e2c":
            self.question_label.text = self.current_item["en"]
        else:
            self.question_label.text = self.current_item["cn"]

    def check_answer(self, instance):
        if self.current_item is None:
            return
        user_ans = self.answer_input.text.strip()
        if self.mode == "e2c":
            right_ans = self.current_item["cn"]
        else:
            right_ans = self.current_item["en"]
        # 统计
        if not store.exists("stat"):
            store.put("stat", total=0, right=0)
        stat = store.get("stat")
        stat["total"] += 1
        if user_ans.lower() == right_ans.lower():
            self.result_label.text = f"✅回答正确！{right_ans}"
            self.result_label.color = RIGHT_COLOR
            stat["right"] +=1
        else:
            self.result_label.text = f"❌答案错误！正确：{right_ans}"
            self.result_label.color = WRONG_COLOR
            # 存入错题本
            if not store.exists("wrong"):
                store.put("wrong", items=[])
            wrong_list = store.get("wrong")["items"]
            if self.current_item not in wrong_list:
                wrong_list.append(self.current_item)
            store.put("wrong", items=wrong_list)
        store.put("stat", total=stat["total"], right=stat["right"])

    def read_aloud(self, instance):
        #安卓Pydroid3调用系统TTS朗读英文，电脑端无效
        try:
            import android
            text = self.question_label.text
            android.tts.speak(text)
        except Exception as e:
            self.result_label.text = "电脑端不支持朗读，手机Pydroid3可用"

    def add_fav(self, instance):
        if not self.current_item:
            return
        if not store.exists("fav"):
            store.put("fav", items=[])
        fav_list = store.get("fav")["items"]
        if self.current_item not in fav_list:
            fav_list.append(self.current_item)
            store.put("fav", items=fav_list)
            self.result_label.text = "⭐已收藏！"

#收藏页面
class FavScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        #修复背景
        with layout.canvas.before:
            Color(*BG_COLOR)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        def update_rect(instance, value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size
        layout.bind(pos=update_rect, size=update_rect)
        self.add_widget(layout)
        title = Label(text="⭐收藏单词句子", font_name=FONT_NAME, font_size=FONT_SIZE_BIG, color=TEXT_COLOR, size_hint_y=0.1)
        layout.add_widget(title)
        scroll = ScrollView()
        self.scroll_layout = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter("height"))
        scroll.add_widget(self.scroll_layout)
        layout.add_widget(scroll)
        btn_back = Button(text="返回主页", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL, size_hint_y=0.08)
        btn_back.bind(on_press=lambda x: setattr(sm, "current", "main"))
        layout.add_widget(btn_back)

    def load_data(self):
        self.scroll_layout.clear_widgets()
        if store.exists("fav"):
            fav_items = store.get("fav")["items"]
            for item in fav_items:
                txt = Label(text=f"{item['en']} | {item['cn']}", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL, color=TEXT_COLOR, size_hint_y=None, height=60)
                self.scroll_layout.add_widget(txt)

#错题本页面
class WrongScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        #修复背景
        with layout.canvas.before:
            Color(*BG_COLOR)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        def update_rect(instance, value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size
        layout.bind(pos=update_rect, size=update_rect)
        self.add_widget(layout)
        title = Label(text="❌错题本", font_name=FONT_NAME, font_size=FONT_SIZE_BIG, color=TEXT_COLOR, size_hint_y=0.1)
        layout.add_widget(title)
        scroll = ScrollView()
        self.scroll_layout = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter("height"))
        scroll.add_widget(self.scroll_layout)
        layout.add_widget(scroll)
        btn_back = Button(text="返回主页", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL, size_hint_y=0.08)
        btn_back.bind(on_press=lambda x: setattr(sm, "current", "main"))
        layout.add_widget(btn_back)

    def load_data(self):
        self.scroll_layout.clear_widgets()
        if store.exists("wrong"):
            wrong_items = store.get("wrong")["items"]
            for item in wrong_items:
                txt = Label(text=f"{item['en']} | {item['cn']}", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL, color=TEXT_COLOR, size_hint_y=None, height=60)
                self.scroll_layout.add_widget(txt)

#统计页面
class StatScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        #修复背景
        with layout.canvas.before:
            Color(*BG_COLOR)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        def update_rect(instance, value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size
        layout.bind(pos=update_rect, size=update_rect)
        self.add_widget(layout)
        self.stat_label = Label(text="学习统计", font_name=FONT_NAME, font_size=FONT_SIZE_BIG, color=TEXT_COLOR)
        layout.add_widget(self.stat_label)
        btn_back = Button(text="返回主页", font_name=FONT_NAME, font_size=FONT_SIZE_NORMAL, size_hint_y=0.08)
        btn_back.bind(on_press=lambda x: setattr(sm, "current", "main"))
        layout.add_widget(btn_back)

    def load_stat(self):
        if store.exists("stat"):
            data = store.get("stat")
            total = data["total"]
            right = data["right"]
            if total == 0:
                rate = 0
            else:
                rate = round(right / total *100,1)
            self.stat_label.text = f"总答题：{total}题\n答对：{right}题\n正确率：{rate}%"

# 注册全部页面
sm.add_widget(MainScreen(name="main"))
sm.add_widget(WordScreen(name="word"))
sm.add_widget(FavScreen(name="fav"))
sm.add_widget(WrongScreen(name="wrong"))
sm.add_widget(StatScreen(name="stat"))

class EnglishStudyApp(App):
    def build(self):
        Window.clearcolor = BG_COLOR
        return sm

if __name__ == "__main__":
    EnglishStudyApp().run()

from flask import Flask
from flask_restx import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app, version='1.0', title='North Korea Information API', description='Information about politics, society, culture, and economy in North Korea')
CORS(app)

# Sample data for each category
politics_data = {'info': '북한 체제의 가장 중요한 특징은 1당 지배, 유일 지배, 세습 지배 세가지 이다. 1당 지배는 과거 사회주의권 국가들의 보편적인 특징으로 집권당이 권력의 최상부에 자리잡고 사실상 입법 행정 사법 3권을 지배하는 체제이며 북한의 지배정당은 조선로동당이다.유일 지배는 독재 정권의 특징으로 당 내에서도 그 권력이 1인에게 집중되어 있는 것을 말한다. 북한의 유일한 중심인 수령은 절대적 지위와 역하을 지닌다. 세습지배는 수령의 자리를 자신의 자손에게 물려주어 세습하는 것을 말한다. 수령으로서 사상, 자질, 능력을 이어받았다는 령도의 계승성이 세습의 근거이다.'}
society_data = {'info': '북한의 주민들은 여행증이 없다면 국내에서도 자신이 거주하는 지역 이외의 다른곳을 마음대로 돌아다닐 수 없다. 해외 여행은 원칙적으로 불가능하고 이민 또한 불가능하다. 북한은 완전체주의 국가로 개인보다 공동체를 중요시 여긴다. 이로 인해 집단생화이나 동원이 보편화 되어 있다. 또한 북한은 전국적으로 심각한 식량난과 전력난을 겪고 있다. '}
culture_data = {'info': '북한의 문화와 예술은 대중에게 공산주의 혁명 정신을 가르치는 세뇌의 무기로서 발전했다. 주로 3명의 수령과 그들의 업적을 찬양하는 주제가 주를 이루지만, 남녀 애정을 다루는 청춘 송가 같은 소설이 발표되기도 했다. 북한은 우리의 표준어와 다른 문화어를 새로 만들고 1966년 부터 말 다듬기 운동을 통해 조선말 대사전을 편찬했다. 하지만 분단의 장기화로 인해 남북한의 언어의 이질화가 심화되고 있다. '}
economy_data = {'info': '북한의 경제는 정부 주도의 계획 경제 체제로, 중앙 정부에서 수립된 경제 개발 계획이 지방 정부와 공장 및 기업소 등에서 엄격하게 집행되는 일원화된 경제 체계를 갖추고 있다. 북한 경제의 또 다른 중요한 기조는 ‘중공업 우선 발전, 경공업 · 농업의 동시 발전’이다. 그러나 이 원칙은 한정된 자본과 자원으로 인하여 현실에서는 중공업 우선 노선으로 나타났다. 경공업  농업의 발전이 동반되지 않은 중공업 우선 발전 전략의 한계는 1990년 사회주의 경제권 붕괴와 함께 심각하게 드러났고, 1990년대 중반 심각한 경제난과 식량난으로 이어졌다. 북한 경제는 1999년 이후 회복세를 보였으나, 2006년 이후 정체되는 추세이다.'}

@api.route('/politics')
class Politics(Resource):
    def get(self):
        return politics_data

@api.route('/society')
class Society(Resource):
    def get(self):
        return society_data

@api.route('/culture')
class Culture(Resource):
    def get(self):
        return culture_data

@api.route('/economy')
class Economy(Resource):
    def get(self):
        return economy_data

if __name__ == '__main__':
    app.run(debug=True)

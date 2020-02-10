#! python3
#! randomQuizGenerator.py - ランダム順に問題と答えを並べ問題集と回答集を作る

import random

# 問題のデータ　キーが都道府県で、値が県庁所在地

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 35この問題集を作成する
for quiz_num in range(35):
    #TODO: 問題集と回答集のファイルを作成する
    quiz_file = open('capitalsquiz{}.txt'.format(quiz_num + 1), 'w')
    answer_key_file = open('capitalsquiz_answers{}.txt'.format(quiz_num + 1), 'w')

    #TODO: 問題集のヘッダーを書く
    quiz_file.write('名前:\n\n日付:\n\n学期:\n\n')
    quiz_file.write((' ' * 20) + '都道府県クイズ(問題番号{})'.format(quiz_num + 1))
    quiz_file.write('\n\n')

    #TODO: 都道府県の順番をシャッフルする
    prefectures = list(capitals.keys())
    random.shuffle(prefectures)

    #TODO: 47都道府県をループして、それぞれ問題を作成する
    for question_num in range(len(prefectures)):
        # 正解と誤答を取得する
        correct_answer = capitals[prefectures[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

    #TODO 問題文と回答選択肢を問題ファイルに書く
        quiz_file.write('{}. {}の都道府県庁所在地は？\n'.format(question_num + 1,
            prefectures[question_num]))
        for i in range(4):
            quiz_file.write(' {}.{}\n'.format('ABCD'[i], answer_options[i]))

        quiz_file.write('\n')

    #TODO 答えの選択肢を回答ファイルに書く
        answer_key_file.write('{}. {}\n'.format(question_num + 1, 'ABCD'[
            answer_options.index(correct_answer)
        ]))

    quiz_file.close()
    answer_key_file.close()

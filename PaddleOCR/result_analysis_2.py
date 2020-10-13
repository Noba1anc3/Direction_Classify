

num = {'chepiao': [0, 0, 0, 0, 0, 0, 0, 0],
       'chuzuchefapiao': [0, 0, 0, 0, 0, 0, 0, 0],
       'dianzishu': [0, 0, 0, 0, 0, 0, 0, 0],
       'jiaocai': [0, 0, 0, 0, 0, 0, 0, 0],
       'jipiao': [0, 0, 0, 0, 0, 0, 0, 0],
       'menpiao': [0, 0, 0, 0, 0, 0, 0, 0],
       'mingpian': [0, 0, 0, 0, 0, 0, 0, 0],
       'muji': [0, 0, 0, 0, 0, 0, 0, 0],
       'niandubaogao': [0, 0, 0, 0, 0, 0, 0, 0],
       'shenfenzheng': [0, 0, 0, 0, 0, 0, 0, 0],
       'shijuan': [0, 0, 0, 0, 0, 0, 0, 0],
       'shouju': [0, 0, 0, 0, 0, 0, 0, 0],
       'tijianbiao': [0, 0, 0, 0, 0, 0, 0, 0],
       'jiashizheng': [0, 0, 0, 0, 0, 0, 0, 0],
       'yingyezhizhao': [0, 0, 0, 0, 0, 0, 0, 0],
       'yinhangliushui': [0, 0, 0, 0, 0, 0, 0, 0],
       'zengzhishuifapiao': [0, 0, 0, 0, 0, 0, 0, 0],
       'pingjibaogao': [0, 0, 0, 0, 0, 0, 0, 0],
       }

Piaoju = {'chepiao', 'chuzuchefapiao', 'jipiao', 'menpiao', 'shouju', 'zengzhishuifapiao'}
piaoju = [0, 0, 0, 0, 0, 0, 0, 0]
Certificate = {'mingpian', 'shenfenzheng', 'jiashizheng', 'yingyezhizhao'}
certificate = [0, 0, 0, 0, 0, 0, 0, 0]
Docu = {'dianzishu', 'jiaocai', 'muji', 'yinhangliushui', 'pingjibaogao', 'niandubaogao'}
docu = [0, 0, 0, 0, 0, 0, 0, 0]
Other = {'shijuan', 'tijianbiao'}
other = [0, 0, 0, 0, 0, 0, 0, 0]

labels = []
preds = []

with open('./label.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
           labels.append([line.split(' ')[0], line.split(' ')[1].split('\n')[0]])
f.close()

with open('./result.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
           preds.append([line.split(' ')[0], line.split(' ')[4].split('\n')[0], line.split(' ')[1], line.split(' ')[3]])
f.close()


wrong_ratio_all = []
wrong_ratio_wrong = 0
wrong_ratio_right = 0
falseNum = 0
wrong_ratio_falseNum = 0
wrong_ratio_trueNum = 0

with open('./result.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
           wrong_ratio_all.append(float(line.split(' ')[2]))
f.close()

for i, pred in enumerate(preds):

    pred_name = pred[0].split('.jp')[0]
    label = ''
    for l in labels:
        if l[0] == pred_name:
            label = l
            break

    if label[1] != pred[1]:
        falseNum += 1
        if wrong_ratio_all[i] != 0:
            wrong_ratio_falseNum += 1
            wrong_ratio_wrong += wrong_ratio_all[i]
    if label[1] == pred[1]:
        if wrong_ratio_all[i] != 0:
            wrong_ratio_trueNum += 1
            wrong_ratio_right += wrong_ratio_all[i]

print('错误图片总数:', falseNum,
      '错误仿射变换总数:', wrong_ratio_falseNum,
      '错误仿射变换占比:', '%.2f' % (wrong_ratio_falseNum*100/falseNum) + '%',
      '平均错误仿射变换比例:', wrong_ratio_wrong/wrong_ratio_falseNum)
print('正确图片总数:', 3600 - falseNum,
      '错误仿射变换总数:', wrong_ratio_trueNum,
      '错误仿射变换占比:', '%.2f' % (wrong_ratio_trueNum*100 / (3600 - falseNum)) + '%',
      '平均错误仿射变换比例:', '%.2f' % (wrong_ratio_right/wrong_ratio_trueNum))

phase_1_time = 0
phase_1_min = 1000
phase_1_max = 0
phase_2_time = 0
phase_2_min = 1000
phase_2_max = 0
total_time = 0
total_min = 1000
total_max = 0

minus300 = 0
minus500 = 0
minus1000 = 0
minus2000 = 0

for i, pred in enumerate(preds):
       phase_1_time += float(pred[2])
       phase_2_time += float(pred[3])
       total_time += float(pred[2]) + float(pred[3])

       if float(pred[2]) + float(pred[3]) < 300:
           minus300 += 1
       elif float(pred[2]) + float(pred[3]) < 500:
           minus500 += 1
       elif float(pred[2]) + float(pred[3]) < 1000:
           minus1000 += 1
       elif float(pred[2]) + float(pred[3]) < 2000:
           minus2000 += 1

       if float(pred[2]) < phase_1_min:
           phase_1_min = float(pred[2])
       if float(pred[2]) > phase_1_max:
           phase_1_max = float(pred[2])
       if float(pred[3]) < phase_2_min:
           phase_2_min = float(pred[3])
       if float(pred[3]) > phase_2_max:
           phase_2_max = float(pred[3])
       if float(pred[2]) + float(pred[3]) < total_min:
           total_min = float(pred[2]) + float(pred[3])
       if float(pred[2]) + float(pred[3]) > total_max:
           total_max = float(pred[2]) + float(pred[3])

       pred_name = pred[0].split('.jp')[0]
       label = ''
       for l in labels:
              if l[0] == pred_name:
                     label = l
                     break
       #label = labels[i]
       cls = pred[0].split('_')[0]
       if cls == 'yibao':
              cls = 'jiashizheng'

       label_direction = int(label[1])
       pred_direction = int(pred[1])
       num[cls][label_direction*2+1] += 1
       if label_direction == pred_direction:
              num[cls][pred_direction*2] += 1

print('\n检测时间最少:', phase_1_min, '检测时间最多:', phase_1_max, '检测时间平均:', '%.2f' % (phase_1_time / 3600))
print('分类时间最少:', phase_2_min, '分类时间最多:', phase_2_max, '分类时间平均:', '%.2f' % (phase_2_time / 3600))
print('总时间最少:', total_min, '总时间最多:', total_max, '总时间平均:', '%.2f' % (total_time / 3600))
print('低于300ms:', '%.2f' % (minus300/36) + '%', '低于500ms:', '%.2f' % (minus500/36) + '%', '低于1000ms:', '%.2f' % (minus1000/36) + '%', '低于2000ms', '%.2f' % (minus2000/36) + '%')
all_correct = 0
all = 0
for key in num:
       all_correct += (num[key][0]+num[key][2]+num[key][4]+num[key][6])
       all += (num[key][1]+num[key][3]+num[key][5]+num[key][7])

print('\n总准确率:', '%.2f' % (all_correct*100 / all), '\n')

for i, key in enumerate(Piaoju):
       piaoju[0] += num[key][0]
       piaoju[1] += num[key][1]
       piaoju[2] += num[key][2]
       piaoju[3] += num[key][3]
       piaoju[4] += num[key][4]
       piaoju[5] += num[key][5]
       piaoju[6] += num[key][6]
       piaoju[7] += num[key][7]

print('票据\n',
      '%.2f' % (piaoju[0]*100/piaoju[1]),
      '%.2f' % (piaoju[4]*100/piaoju[5]),
      '%.2f' % (piaoju[2]*100/piaoju[3]),
      '%.2f' % (piaoju[6]*100/piaoju[7]),
      '%.2f' % ((piaoju[0] + piaoju[2] + piaoju[4] + piaoju[6]) / 12), '\n')

for i, key in enumerate(Certificate):
       certificate[0] += num[key][0]
       certificate[1] += num[key][1]
       certificate[2] += num[key][2]
       certificate[3] += num[key][3]
       certificate[4] += num[key][4]
       certificate[5] += num[key][5]
       certificate[6] += num[key][6]
       certificate[7] += num[key][7]

print('证件\n',
      '%.2f' % (certificate[0]*100/certificate[1]),
      '%.2f' % (certificate[4]*100/certificate[5]),
      '%.2f' % (certificate[2]*100/certificate[3]),
      '%.2f' % (certificate[6]*100/certificate[7]),
      '%.2f' % ((certificate[0] + certificate[2] + certificate[4] + certificate[6]) / 8), '\n')

for i, key in enumerate(Docu):
       docu[0] += num[key][0]
       docu[1] += num[key][1]
       docu[2] += num[key][2]
       docu[3] += num[key][3]
       docu[4] += num[key][4]
       docu[5] += num[key][5]
       docu[6] += num[key][6]
       docu[7] += num[key][7]

print('文档\n',
      '%.2f' % (docu[0]*100/docu[1]),
      '%.2f' % (docu[4]*100/docu[5]),
      '%.2f' % (docu[2]*100/docu[3]),
      '%.2f' % (docu[6]*100/docu[7]),
      '%.2f' % ((docu[0] + docu[2] + docu[4] + docu[6]) / 12), '\n')

for i, key in enumerate(Other):
       other[0] += num[key][0]
       other[1] += num[key][1]
       other[2] += num[key][2]
       other[3] += num[key][3]
       other[4] += num[key][4]
       other[5] += num[key][5]
       other[6] += num[key][6]
       other[7] += num[key][7]

print('其他\n',
      '%.2f' % (other[0]*100/other[1]),
      '%.2f' % (other[4]*100/other[5]),
      '%.2f' % (other[2]*100/other[3]),
      '%.2f' % (other[6]*100/other[7]),
      '%.2f' % ((other[0] + other[2] + other[4] + other[6]) / 4), '\n')

print('方向 上 ',
      '%.2f' % ((other[0] + docu[0] + certificate[0] + piaoju[0])*100 / (other[1] + docu[1] + certificate[1] + piaoju[1])),
      '\n方向 下 ',
      '%.2f' % ((other[4] + docu[4] + certificate[4] + piaoju[4])*100 / (other[5] + docu[5] + certificate[5] + piaoju[5])),
      '\n方向 左 ',
      '%.2f' % ((other[2] + docu[2] + certificate[2] + piaoju[2])*100 / (other[3] + docu[3] + certificate[3] + piaoju[3])),
      '\n方向 右 ',
      '%.2f' % ((other[6] + docu[6] + certificate[6] + piaoju[6])*100 / (other[7] + docu[7] + certificate[7] + piaoju[7])),
      '\n')

for i, key in enumerate(num):
    if key in Piaoju:
        print('| ' + key + ' | ',
              '%.2f' % (num[key][0]*100 / num[key][1]) + ' |',
              '%.2f' % (num[key][4]*100 / num[key][5]) + ' |',
              '%.2f' % (num[key][2]*100 / num[key][3]) + ' |',
              '%.2f' % (num[key][6]*100 / num[key][7]) + ' |',
              '%.2f' % ((num[key][0] + num[key][2] + num[key][4] + num[key][6])*100 /
                                (num[key][1] + num[key][3] + num[key][5] + num[key][7])) + ' |')
print('\n')

for i, key in enumerate(num):
    if key in Certificate:
        print('| ' + key + ' | ',
              '%.2f' % (num[key][0]*100 / num[key][1]) + ' |',
              '%.2f' % (num[key][4]*100 / num[key][5]) + ' |',
              '%.2f' % (num[key][2]*100 / num[key][3]) + ' |',
              '%.2f' % (num[key][6]*100 / num[key][7]) + ' |',
              '%.2f' % ((num[key][0] + num[key][2] + num[key][4] + num[key][6])*100 /
                                (num[key][1] + num[key][3] + num[key][5] + num[key][7])) + ' |')
print('\n')

for i, key in enumerate(num):
    if key in Docu:
        print('| ' + key + ' | ',
              '%.2f' % (num[key][0]*100 / num[key][1]) + ' |',
              '%.2f' % (num[key][4]*100 / num[key][5]) + ' |',
              '%.2f' % (num[key][2]*100 / num[key][3]) + ' |',
              '%.2f' % (num[key][6]*100 / num[key][7]) + ' |',
              '%.2f' % ((num[key][0] + num[key][2] + num[key][4] + num[key][6])*100 /
                                (num[key][1] + num[key][3] + num[key][5] + num[key][7])) + ' |')
print('\n')

for i, key in enumerate(num):
    if key in Other:
        print('| ' + key + ' | ',
              '%.2f' % (num[key][0]*100 / num[key][1]) + ' |',
              '%.2f' % (num[key][4]*100 / num[key][5]) + ' |',
              '%.2f' % (num[key][2]*100 / num[key][3]) + ' |',
              '%.2f' % (num[key][6]*100 / num[key][7]) + ' |',
              '%.2f' % ((num[key][0] + num[key][2] + num[key][4] + num[key][6])*100 /
                                (num[key][1] + num[key][3] + num[key][5] + num[key][7])) + ' |')


doc_correct, lr_correct, ud_correct, lr_total, ud_total = 0, 0, 0, 0, 0
for i, pred in enumerate(preds):

    pred_name = pred[0].split('.jp')[0]
    label = ''
    for l in labels:
        if l[0] == pred_name:
            label = l
            break

    if label[1] in ['0', '2']:
        lr_total += 1
        if pred[1] in ['0', '2']:
            doc_correct += 1
            lr_correct += 1
    elif label[1] in ['1', '3']:
        ud_total += 1
        if pred[1] in ['1', '3']:
            doc_correct += 1
            ud_correct += 1

print('\n文档朝向准确率:', '%.2f' % (doc_correct/36))
print('上下朝向准确率:', '%.2f' % (lr_correct*100/lr_total))
print('左右朝向准确率:', '%.2f' % (ud_correct*100/ud_total))

dir_correct, forward_correct, reverse_correct, forward_total, reverse_total = 0, 0, 0, 0, 0
for i, pred in enumerate(preds):

    pred_name = pred[0].split('.jp')[0]
    label = ''
    for l in labels:
        if l[0] == pred_name:
            label = l
            break

    if label[1] in ['1', '2']:
        reverse_total += 1
        if pred[1] in ['1', '2']:
            dir_correct += 1
            reverse_correct += 1
    elif label[1] in ['0', '3']:
        forward_total += 1
        if pred[1] in ['0', '3']:
            dir_correct += 1
            forward_correct += 1

print('\n文字方向准确率:', '%.2f' % (dir_correct/36))
print('正向文字准确率:', '%.2f' % (forward_correct*100/forward_total))
print('反向文字准确率:', '%.2f' % (reverse_correct*100/reverse_total))

up, rt, dn, lt = [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]
up_total, rt_total, dn_total, lt_total = 0, 0, 0, 0
for i, pred in enumerate(preds):

    pred_name = pred[0].split('.jp')[0]
    label = ''
    for l in labels:
        if l[0] == pred_name:
            label = l
            break

    if label[1] == '0':
        up_total += 1
        up[int(pred[1])] += 1
    elif label[1] == '1':
        lt_total += 1
        lt[int(pred[1])] += 1
    elif label[1] == '2':
        dn_total += 1
        dn[int(pred[1])] += 1
    elif label[1] == '3':
        rt_total += 1
        rt[int(pred[1])] += 1

print('\n上向文档', '%.2f' % (up[0]*100/up_total), '%.2f' % (up[2]*100/up_total),
      '%.2f' % (up[1]*100/up_total), '%.2f' % (up[3]*100/up_total))

print('下向文档', '%.2f' % (dn[0]*100/dn_total), '%.2f' % (dn[2]*100/dn_total),
      '%.2f' % (dn[1]*100/dn_total), '%.2f' % (dn[3]*100/dn_total))

print('左向文档', '%.2f' % (lt[0]*100/lt_total), '%.2f' % (lt[2]*100/lt_total),
      '%.2f' % (lt[1]*100/lt_total), '%.2f' % (lt[3]*100/lt_total))

print('右向文档', '%.2f' % (rt[0]*100/rt_total), '%.2f' % (rt[2]*100/rt_total),
      '%.2f' % (rt[1]*100/rt_total), '%.2f' % (rt[3]*100/rt_total))

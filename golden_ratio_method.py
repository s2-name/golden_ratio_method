import numexpr as nx

# Функция проверки чтроки на содержание (дробного) числа
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

#Начальная функция, которая принимает данные и раскидывает их по переменным (она же возвращает ответ)
def dataIn(data):
    global func
    dataList = data.split()
    if len(dataList) == 4:
        func = dataList[0]
        a, b, e = dataList[1:]

        # Константы и счётчик иттераций
        R1 = 0.382
        R2 = 0.618
        n = 0

        #Проверка, ввёл ли пользователь данные верно
        if isfloat(a) and isfloat(b) and isfloat(e):
            a, b, e = float(a), float(b), float(e)
            # эта переменная хранит весь ответ
            res = f"Входные данные: функция {func}, отрезок [{a}, {b}], E {e}\n"
            step1(a, b, e, R1, R2, n, res)
            return responce
        else:
            return "Введены неверные данные"
    else:
        return "Введены неверные данные"


# Функция считает исходную функцию (ппц объяснил), если функция неправильная, программа выдаст False
def solve_function(x):
    global func
    try:
        # Эта строка преобразует строку в выражение и считает его
        resl = nx.evaluate(func)
        # Конвертируем в число и обрезаем до 3 знаков после запятой
        resl = round(float(resl), 3)
        return resl
    except:
        return False

# Первый шаг
def step1(a, b, e, R1, R2, n, res):
    global responce
    # ищем дельту, x, y
    delt = b - a
    x = round(a + R1 * delt, 3)
    y = round(a + R2 * delt, 3)

    #Ищем функции от x и y
    Fx = solve_function(x)
    Fy = solve_function(y)

    #Если функция верная, то продолжаем
    if Fx:
        res = res + f"<b><i>1.1</i></b>\nD={b}-{a}=<b>{delt}</b>\nX={a}+{R1}*{delt}=<b>{x}</b>\nY={a}+{R2}*{delt}=<b>{y}\n<i>1.2</i></b>\nf(x)=<b>{Fx}</b>\nf(y)=<b>{Fy}</b>\n"
        step2(a, b, e, R1, R2, x, y, Fx, Fy, n, res)
    else:
        responce = "Введены неверные данные!"

# Второй шаг
def step2(a, b, e, R1, R2, x, y, Fx, Fy, n, res):
    #Прибавляем счётчик
    n += 1
    res = res + f"<b><i>{n}.3</i></b>\n"
    #Выбираем какой шаг следующий
    if Fx <= Fy:
        res = res + f"{Fx} &lt;= {Fy} =&gt; шаг 4\n"
        step3(a, b, e, R1, R2, x, y, Fx, Fy, n, res)
    else:
        res = res + f"{Fx} &gt; {Fy} =&gt; шаг 5\n"
        step4(a, b, e, R1, R2, x, y, Fx, Fy, n, res)


def step3(aOld, bOld, e, R1, R2, xOld, yOld, FxOld, FyOld, n, res):
    global responce
    a = aOld
    b = yOld
    delt = round(b - a, 3)
    res = res + f"<b><i>{n}.4</i></b>\na=<b>{a}</b>\nb=<b>{b}</b>\nD={b}-{a}=<b>{delt}</b>\n"
    #Если дельта меньше эпсилона, то прекращаем работу возвращаем ответ
    if delt < e:
        responce = res + f"<b>Ответ: X={xOld}, f(x)={solve_function(xOld)}</b>"
    else:
        y = xOld
        Fy = FxOld
        x = round(a + R1 * delt, 3)
        Fx = solve_function(x)
        res = res + f"Y=<b>{y}</b>\nX=<b>{x}</b>\nf(y)=<b>{Fy}</b>\nf(x)=<b>{Fx}</b>\n"
        step2(a, b, e, R1, R2, x, y, Fx, Fy, n, res)


def step4(aOld, bOld, e, R1, R2, xOld, yOld, FxOld, FyOld, n, res):
    a = xOld
    b = bOld
    delt = round(b - a, 3)
    res = res + f"<b><i>{n}.5</i></b>\na=<b>{a}</b>\nb=<b>{b}</b>\nD={b}-{a}=<b>{delt}</b>\n"
    if delt < e:
        res = res + f"<b>Ответ: X {xOld}, f(x) {solve_function(xOld)}</b>"
    else:
        x = yOld
        Fx = FyOld
        y = round(a + R2 * delt, 3)
        Fy = solve_function(y)
        res = res + f"Y=<b>{y}</b>\nX=<b>{x}</b>\nf(y)=<b>{Fy}</b>\nf(x)=<b>{Fx}</b>\n"
        step2(a, b, e, R1, R2, x, y, Fx, Fy, n, res)


if __name__ == "__main__":
    # step1(a, b, e, R1, R2, n)
    data = input('Введите исходные данные в формате <2*x**2+13*x 0 2 0.25>. Степень обозначается двойным умножением, не допускается использование посторонних символов кроме x,  не допускаются пробелы перед и в формуле. Отрезок указывается через пробел, последнее значение - это эпсилон ')
    print(dataIn(data))

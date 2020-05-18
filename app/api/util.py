def model_to_dict(result):
    from collections import Iterable
    # 转换完成后，删除  '_sa_instance_state' 特殊属性
    try:
        if isinstance(result, Iterable):
            tmp = [dict(zip(res.__dict__.keys(), res.__dict__.values())) for res in result]
            for t in tmp:
                t.pop('_sa_instance_state')
        else:
            print(result.__dict__.values())
            tmp = dict(zip(result.__dict__.keys(), result.__dict__.values()))
            tmp.pop('_sa_instance_state')
        return tmp
    except BaseException as e:
        raise TypeError('Type error of parameter')
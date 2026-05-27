def numberOfEmployeesWhoMetTarget( hours, target):
        count = 0

        for h in hours:
            if h >= target:
                count += 1

        return count

hours = [0, 1, 2, 3, 4]
target = 2
print(numberOfEmployeesWhoMetTarget(hours, target))
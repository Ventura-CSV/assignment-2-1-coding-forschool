def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc, f_perc, nb_perc for your results
    ##################################################
    """
    students = int(input("Enter Number of Total Students"))
    males = int(input("Enter Total Numbers of Males"))
    females = int(input("Enter Total Numbers of Females"))
    NonBinary = int(input("Enter Total Numbers of Non-Binary"))
    
    m_perc = (males / students)*100
    f_perc = (females / students)*100
    nb_perc = (NonBinary / students)*100
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    print(f'The total number of students: {students}')
    print(f'The Number of males, females and non-binary: \t{males}\t{females}\t{NonBinary}')
    print(
        f'The percentage of males, females and non-binary: \t {m_perc: .2f}% \t {f_perc: .2f}% \t {nb_perc: .2f}%')
    return m_perc, f_perc, nb_perc


if __name__ == '__main__':
    main()

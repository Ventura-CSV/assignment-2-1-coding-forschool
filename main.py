def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc, f_perc, nb_perc for your results
    ##################################################
    """
    students = int(input("Enter Number of Total Students"))
    m = int(input("Enter Total Numbers of Males"))
    f = int(input("Enter Total Numbers of Females"))
    nb = int(input("Enter Total Numbers of Non-Binary"))
    
    m_perc = (m / students)*100
    f_perc = (f / students)*100
    nb_perc = (nb / students)*100
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    print(f'The total number of students: {students}')
    print(f'The Number of males, females and non-binary: \t{m}\t{f}\t{nb}')
    print(
        f'The percentage of males, females and non-binary: \t {m_perc: .2f} \t {f_perc: .2f} \t {nb_perc: .2f}')
    return m_perc, f_perc, nb_perc


if __name__ == '__main__':
    main()

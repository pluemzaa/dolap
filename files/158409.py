<?xml version="1.0"?>
<flowgorithm fileversion="3.0">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="bamboo"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 09:24:34 "/>
        <attribute name="created" value="YmFtYm9vO01BQ0JPT0tBSVJCQU07MjU2OC0wNy0yMjsiMDk6MTQ6NTEgIjsyNzY3"/>
        <attribute name="edited" value="YmFtYm9vO01BQ0JPT0tBSVJCQU07MjU2OC0wNy0yMjsiMDk6MjQ6MzQgIjsxOzI4Nzc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="interest, years, totalYears" type="Integer" array="False" size=""/>
            <assign variable="years" expression="1"/>
            <declare name="afterlnterest, money, money1, money2, money3, amount" type="Real" array="False" size=""/>
            <output expression="&quot; Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <assign variable="amount" expression="money"/>
            <output expression="&quot; Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot; Input years: &quot;" newline="True"/>
            <input variable="totalYears"/>
            <while expression="years &lt;= totalYears">
                <assign variable="amount" expression="amount + (amount * (interest/100))"/>
                <output expression="&quot;Year &quot; &amp; years &amp;&quot;: &quot; &amp; amount" newline="True"/>
                <assign variable="years" expression="years + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>
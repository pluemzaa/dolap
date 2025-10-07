<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="compound_interest_calculator"/>
        <attribute name="authors" value=""/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 06:58:57 PM"/>
        <attribute name="created" value="dG9ud2E7REVTS1RPUC04N0hRN1BBOzIwMjUtMDctMTY7MDg6MzM6NTggUE07Mjg5NA=="/>
        <attribute name="edited" value="dG9ud2E7REVTS1RPUC04N0hRN1BBOzIwMjUtMDctMjI7MDY6NTg6NTcgUE07MTc7MzA1OA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, currentBalance, initialMoney, interestRate, tempBalance" type="Real" array="False" size=""/>
            <declare name="years, i, tempInt, finalDisplayBalance" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="initialMoney"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interestRate"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="currentBalance" expression="initialMoney"/>
            <for variable="i" start="1" end="years" direction="inc" step="1">
                <assign variable="currentBalance" expression="currentBalance * (1 + interestRate / 100)"/>
                <assign variable="tempBalance" expression="currentBalance * 100"/>
                <assign variable="tempInt" expression="tempBalance"/>
                <assign variable="finalDisplayBalance" expression="tempInt / 100"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;: &quot; &amp; finalDisplayBalance" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>
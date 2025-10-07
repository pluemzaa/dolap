<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="interest"/>
        <attribute name="authors" value="MoZart"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 12:30:20 PM"/>
        <attribute name="created" value="TW9aYXJ0O0pJTk5ZSkFYTE5XWkEwMDsyMDI1LTA3LTE3OzEyOjE3OjA1IFBNOzMwMDA="/>
        <attribute name="edited" value="TW9aYXJ0O0pJTk5ZSkFYTE5XWkEwMDsyMDI1LTA3LTE3OzEyOjMwOjIwIFBNOzM7MzEwMg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Year, Years, i" type="Integer" array="False" size=""/>
            <declare name="money, interest" type="Real" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="Years" expression="1"/>
            <while expression="Year &gt; i">
                <output expression="&quot;Year &quot; &amp; years &amp; &quot; : &quot;" newline="False"/>
                <assign variable="years" expression="years + 1"/>
                <assign variable="money" expression="money * (1+(interest/100))"/>
                <assign variable="i" expression="i + 1"/>
                <output expression="money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>
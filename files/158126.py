<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="683380460-1_3"/>
        <attribute name="authors" value="acer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 06:55:43 PM"/>
        <attribute name="created" value="YWNlcjtMQVBUT1AtNzFQQ09EM0w7MjU2OC0wNy0yMTswNDozNzozNSBQTTsyNzQy"/>
        <attribute name="edited" value="YWNlcjtMQVBUT1AtNzFQQ09EM0w7MjU2OC0wNy0yMTswNjo1NTo0MyBQTTs0OzI4NTQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest" type="Real" array="False" size=""/>
            <declare name="years, year" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="year" expression="1"/>
            <while expression="year &lt;= years">
                <assign variable="money" expression="money * (1 + interest / 100)"/>
                <output expression="&quot;year &quot; &amp; year &amp; &quot;: &quot; &amp; int(money * 100 + 0.5) / 100" newline="True"/>
                <assign variable="year" expression="year + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>
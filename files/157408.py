<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="compound_interest"/>
        <attribute name="authors" value=""/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 05:16:34 PM"/>
        <attribute name="created" value="QVNVUztMQVBUT1AtTlZMOE00QlQ7MjU2OC0wNy0xODswNDo1ODozMyBQTTsyNzA0"/>
        <attribute name="edited" value="QVNVUztMQVBUT1AtTlZMOE00QlQ7MjU2OC0wNy0xODswNToxNjozNCBQTTsyOzI4MDk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="year, i, years" type="Integer" array="False" size=""/>
            <declare name="money, inst" type="Real" array="False" size=""/>
            <assign variable="i" expression="1"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="inst"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="years" expression="0"/>
            <while expression="year &gt;= i">
                <assign variable="years" expression="years + 1"/>
                <assign variable="money" expression="money * (1 + (inst / 100))"/>
                <output expression="&quot;Year &quot; &amp; years &amp; &quot;: &quot; &amp; money" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>
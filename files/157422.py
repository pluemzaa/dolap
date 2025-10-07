<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test4lab4jr"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 09:08:09 PM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLVFDUzFGUUE7MjU2OC0wNy0xODswODo1Mzo1MiBQTTsyNzk4"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLVFDUzFGUUE7MjU2OC0wNy0xODswOTowODowOSBQTTsxOzI5MDk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="original, money, interest, i" type="Real" array="False" size=""/>
            <declare name="year" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="original"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="money" expression="original"/>
            <assign variable="i" expression="1"/>
            <while expression="i &lt;= year">
                <assign variable="money" expression="money * (1 + interest / 100)"/>
                <output expression="&quot;Year &quot;&amp; i &amp;&quot;: &quot;&amp; money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>
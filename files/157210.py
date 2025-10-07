<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_4"/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 10:53:59 PM"/>
        <attribute name="created" value="QWRtaW47Q0FSTEFSOzI1NjgtMDctMTY7MDY6Mjk6NDIgUE07MjIyOA=="/>
        <attribute name="edited" value="QWRtaW47Q0FSTEFSOzI1NjgtMDctMTY7MTA6NTM6NTkgUE07NzsyMzQy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, year" type="Real" array="False" size=""/>
            <declare name="i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest(%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="1"/>
            <while expression="i &lt;= year">
                <assign variable="money" expression="money*(1+interest/100)"/>
                <output expression="&quot;Year&quot;&amp;i&amp;&quot;: &quot;&amp;money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>